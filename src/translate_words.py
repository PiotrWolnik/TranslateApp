from deep_translator import GoogleTranslator

class TranslateWords:
    def __init__(self, text_to_translate: str, language_to_translate_to: str, source_language: str = 'auto'):
        super().__init__()
        self.text_to_translate = text_to_translate
        self.language_to_translate_to = language_to_translate_to
        self.result = GoogleTranslator(source=source_language, 
                                target=self.language_to_translate_to).translate(self.text_to_translate)
    def getResult(self) -> str:
        return self.result
