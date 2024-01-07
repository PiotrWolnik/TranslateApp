screen_manager = """
ScreenManager:
    AnimationScreen
    MenuScreen
    TranslateWordsKV

<CircularProgressBar>
    orientation: "vertical"
    canvas.before:
        Color:
            rgba: root.bar_color + [0.1]
        Line:
            width: root.bar_width
            ellipse: (self.x-190, self.y-175, 600, 600, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_color
        Line:
            width: root.bar_width
            ellipse: (self.x-190, self.y-175, 600, 600, 0, root.set_value*3.6)
    MDLabel:
        text: root.text
        font_name: "BPoppins"
        font_size: "40sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        halign: "center"
        color: 30,155,20/255


<AnimationScreen>
    name: 'animation'
    MDFloatLayout:
        md_bg_color: 100, 20, 248/255, .1
        CircularProgressBar:
            size_hint: None, None
            size: 200, 200
            pos_hint: {"center_x": .5, "center_y": .5}
            value: 100

<MenuScreen>:
    name: 'menu'
    MDBoxLayout:
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        MDLabel:
            text: "Let's translate something !!!"
            font_style: 'H3'
            halign: "center"

    MDRectangleFlatButton:
        text: 'TRANSLATE TEXT'
        padding: ['60dp', '14dp', '60dp', '14dp']
        font_size: "26sp"
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        width: 200
        on_press: root.manager.current = 'translate_words_kv'
    
    MDRectangleFlatButton:
        text: 'TRANSLATE RECORDING'
        padding: ['20dp', '14dp', '20dp', '14dp']
        font_size: "26sp"
        pos_hint: {'center_x': 0.5, 'center_y':0.35}
        width: 200
        on_press: root.manager.current = app.get_transcription()

    MDRectangleFlatButton:
        text: 'TRANSLATE SPEECH'
        padding: ['42dp', '14dp', '42dp', '14dp']
        font_size: "26sp"
        pos_hint: {'center_x': 0.5, 'center_y':0.2}
        width: 200
        on_press: root.manager.current = app.view_translate_speech()

<TranslateWordsKV>:
    name: 'translate_words_kv'
    MDRaisedButton:
        id: button
        text: "Choose target language"
        pos_hint: {"center_x": .5, "center_y": .875}
        on_release: root.dropdown()
    
    MDRaisedButton:
        id: button2
        text: "Choose source language or leave as auto"
        pos_hint: {"center_x": .5, "center_y": .7}
        on_release: root.dropdown_for_source_lang()

    MDTextField:
        id: text_to_translate
        mode: "rectangle"
        multiline: True
        hint_text: "Enter text to translate"
        helper_text_mode: "on_focus"
        icon_right: "android"
        pos_hint: {'center_x':0.5, "center_y":0.5}
        
    MDTextField:
        id: text_translated
        mode: "rectangle"
        multiline: True
        hint_text: "Translated_text"
        helper_text_mode: "on_focus"
        icon_right: "android"
        pos_hint: {'center_x':0.5, "center_y":0.35}
        padding_x:[20,20]
    
    MDRectangleFlatButton:
        text: 'Translate'
        pos_hint: {'center_x': 0.5, 'center_y':0.2}
        on_release: root.translate()

    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y':0.1}
        on_press: root.clear()
        on_release: root.manager.current = 'menu'
"""