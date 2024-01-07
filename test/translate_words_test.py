from unittest import TestCase
from deep_translator import GoogleTranslator
import sys
sys.path.append('../src')
from translate_words import TranslateWords
from Levenshtein import distance
import pytest

text_to_process_auto = [("Guten Morgen!", ), ("Good morning!", ), ("God morgen!", )]
@pytest.mark.parametrize(("arg",), text_to_process_auto)
def testGetResultAutoOption(arg):
    translated = TranslateWords(arg, "pl").getResult()
    assert  translated == "Dzień dobry!"

text_to_process_with_source_lang = [("Hola!", 'es'), ("Salut!", 'fr'), ("Hej!", 'da')]
@pytest.mark.parametrize(("arg1","arg2"), text_to_process_with_source_lang)
def testGetResultSrcLangOption(arg1, arg2):
    translated = TranslateWords(arg1, "pl", arg2).getResult()
    assert  translated == "Cześć!"

translate_long_text = [("Good morning! Today we will look at the work of a future engineer.", ),
                       ("Guten Morgen! Heute schauen wir uns die Arbeit eines zukünftigen Ingenieurs an.", ), 
                       ("Bonjour! Aujourd'hui, nous allons examiner le travail d'un futur ingénieur.", )]
@pytest.mark.parametrize(("arg", ), translate_long_text)
def testGetResultForLongText(arg):
    translated = TranslateWords(arg, "pl").getResult()
    assert  translated == "Dzień dobry! Dziś przyjrzymy się pracy przyszłego inżyniera."


