from unittest import TestCase
from mock import patch
import whisper
import speech_recognition as sr
from translate_words import TranslateWords

class TranslateSpeech:
    def __init__(self, language_to_translate_to: str, audio: str, source_language: str = 'auto') -> None:
        self.language_to_translate_to = language_to_translate_to
        self.source_language = source_language
        model = whisper.load_model("base")
        self.transcription = model.transcribe(audio)
    
    def translate_speech(self) -> str:
        return TranslateWords(self.transcription["text"], self.language_to_translate_to, self.source_language).getResult()

    def get_transcript_of_speech(self) -> str:
        return self.transcription["text"]
    
class TranslateSpeechTest(TestCase):
    @patch("translate_words.TranslateWords.getResult")
    def testGetResultIsCalledFromTranslateSpeech(self, mocked_method):
        speech_translator = TranslateSpeech("en", "audio_samples/kennedy_speech.wav")
        speech_translator.translate_speech()
        assert mocked_method.call_count == 1

    def testGetTranscript(self):
        speech_translator = TranslateSpeech("pl", "audio_samples/audio.wav")
        output_transcript = speech_translator.get_transcript_of_speech().replace(".", "").replace(",", "").lower().strip()
        expected_output = str('''Dzień dobry. Dzisiaj testujemy pracę dyplomanta.''').replace(".", "").lower().strip()
        self.assertEqual(output_transcript, expected_output)

    def testTranslateSpeech(self):
        speech_translator = TranslateSpeech("en", "audio_samples/audio.wav")
        output_translated = speech_translator.translate_speech().replace(".", "").replace(",", "").lower().strip()
        expected_output = str('''Good morning. Today we are testing the work of a diplomat.''').replace(".", "").lower().strip()
        self.assertEqual(output_translated, expected_output)
