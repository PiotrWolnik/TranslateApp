# Location of modules
import sys
sys.path.append('./src')
# Modules to include
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from languages import languages
from languages_for_source_lang import source_languages
from screen_manager import screen_manager
from translate_words import TranslateWords
# from webview import WebView
from android.permissions import request_permissions, Permission
from abc import ABC, abstractmethod
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.clock import Clock
from android.storage import primary_external_storage_path
from kivy.core.text import LabelBase
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty

primary_ext_storage = primary_external_storage_path()

target_language = ""
source_language = "auto"
path_to_recording = ""

class CircularProgressBar(AnchorLayout):
    value = NumericProperty(0)
    set_value = NumericProperty(0)
    bar_color = ListProperty([240/255,150/255,0/255])
    bar_width = NumericProperty(10)
    text = StringProperty("0%")
    duration = NumericProperty(2.5)
    counter = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, *args):
        Clock.schedule_interval(self.percent_counter, self.duration/self.value)
    
    def percent_counter(self, *args):
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:

            Clock.unschedule(self.percent_counter)
            


class AnimationScreen(Screen):
    secs = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, sec):
        self.secs = self.secs+1
        if self.secs == 4:
            self.manager.current = 'menu'

class MenuScreen(Screen):
    pass


class TranslateWordsKV(Screen):
    def dropdown(self):
        menu_items = [
            {
                "text": f"{languages[i][1]}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=languages[i][0]: self.menu_callback(x),
            } for i in range(languages.shape[0])
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def menu_callback(self, language):
        global target_language
        target_language = language
        self.menu.dismiss()
    
    def dropdown_for_source_lang(self):
        menu_items = [
            {
                "text": f"{source_languages[i][1]}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=source_languages[i][0]: self.menu_callback_source_lang(x),
            } for i in range(source_languages.shape[0])
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.button2,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def menu_callback_source_lang(self, language):
        global source_language
        source_language = language
        self.menu.dismiss()
    
    def translate(self):
        global source_language
        translated = TranslateWords(self.ids.text_to_translate.text.strip(), target_language, source_language)
        self.ids.text_translated.text = f"{translated.getResult()}"
        self.ids.text_to_translate.text = ""
        source_language = "auto"

    def clear(self):
        self.ids.text_translated.text = ""


class DemoApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        screen = Builder.load_string(screen_manager)
    
        return screen
    
    def on_start(self):
        request_permissions([Permission.RECORD_AUDIO, Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])

    def view_translate_speech(self):
        import webbrowser
        webbrowser.open('https://speechrecognitionweb-lf4thqhyxpwttuat7ffotl.streamlit.app')

    def get_transcription(self):
        import webbrowser
        webbrowser.open('https://recordingtranslationapp-otnkb2cymzdxypyaozv22p.streamlit.app')

DemoApp().run()
