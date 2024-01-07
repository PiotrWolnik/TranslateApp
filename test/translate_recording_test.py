from unittest import TestCase
from deep_translator import GoogleTranslator
from mock import patch
import whisper
import speech_recognition as sr
from translate_words import TranslateWords
from unittest.mock import Mock

class TranslateRecording:
    def __init__(self, language_to_translate_to: str, audio: str, source_language: str = 'auto') -> None:
        self.language_to_translate_to = language_to_translate_to
        self.source_language = source_language
        self.audio = audio
    
    def translate_full_audio(self) -> str:
        model = whisper.load_model("base")
        transcription = model.transcribe(self.audio)
        return TranslateWords(transcription["text"], self.language_to_translate_to, self.source_language).getResult()

    def translate_part_of_the_audio(self, starting_point: float, ending_point: float) -> str:
        recognizer = sr.Recognizer()
        with sr.AudioFile(self.audio) as source:
            audio_data = recognizer.record(source, offset=starting_point,duration=ending_point)
            transcription = recognizer.recognize_google(audio_data)
        return TranslateWords(transcription, self.language_to_translate_to, self.source_language).getResult()
    
class TranslateRecordingTest(TestCase):
    @patch("translate_words.TranslateWords.getResult")
    def testGetResultIsCalledForFullAudio(self, mocked_method):
        recording_translator = TranslateRecording("en", "audio_samples/kennedy_speech.wav")
        recording_translator.translate_full_audio()
        assert mocked_method.call_count == 1
    
    @patch("translate_words.TranslateWords.getResult")
    def testGetResultIsCalledForPartOfTheAudio(self, mocked_method):
        recording_translator = TranslateRecording("en", "audio_samples/kennedy_speech.wav")
        recording_translator.translate_part_of_the_audio(0, 5)
        assert mocked_method.call_count == 1

    def testTranslateFullAudio(self):
        recording_translator = TranslateRecording('en', "audio_samples/kennedy_speech.wav")
        output_from_translation = recording_translator.translate_full_audio().replace(".", "").lower().strip()
        expected_output = str('''I believe that this nation should commit itself to achieving the goal, before this decade is out, of landing a man on the moon and returning him safely to the Earth. No single space project in this period will be more impressive to mankind or more important for the long range exploration of space.''').replace(",", "").replace(".", "").lower().strip()
        self.assertEqual(output_from_translation, expected_output)

    def testTranslatePartOfTheAudio(self):
        recording_translator = TranslateRecording("en", "audio_samples/kennedy_speech.wav")
        output_from_translation = recording_translator.translate_part_of_the_audio(0, 5).replace(".", "").lower().strip()
        expected_output = str("I believe that this nation should commit itself to achieving the goal.").replace(".", "").lower().strip()
        self.assertEqual(output_from_translation, expected_output)
