from kivy.app import App
from kivy.lang import Builder
from kivy.uix.codeinput import CodeInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.extras.highlight import KivyLexer
from kivy.properties import ObjectProperty

class CodeEditor(CodeInput):
    lexer=KivyLexer()

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        self.readonly = False
        if len(modifiers) and text:

            if modifiers[0] == "ctrl" and ord(text) in [270, 269, 43, 45, 61]:
                self.readonly = True
                if ord(text) in [270, 61, 43]:
                    self.font_size += 1
                    self.cursor = (self.cursor[0] - 1, 0)
                    return
                elif ord(text) in [269, 45]:
                    self.font_size -= 1
                    self.cursor = (self.cursor[0] - 1, 0)
                    return

        return super(CodeEditor, self).keyboard_on_key_down(window, keycode, text, modifiers)

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, key, keycode, text, modifiers):
        if len(modifiers) and text:
            if modifiers[0] == "ctrl" and text in ["s", "l", "p"]:

                if text == "s":
                    self.save_file()
                elif text == "l":
                    self.load_file()
                elif text == "p":
                    self.preview()

    def preview(self):
        preview_area = self.root.preview_area
        code_editor = self.root.code_editor
        preview_area.clear_widgets()

        try:
            preview_area.add_widget(Builder.load_string(code_editor.text))
        except Exception as e:
            preview_area.add_widget(Label(text=(e.message if getattr(e, r"message", None) else str(e))))

    def load_file(self):
        code_editor = self.root.code_editor
        filepath = self.root.filepath.text

        try:
            with open(filepath, "r", encoding="utf8") as file:
                code_editor.text = file.read()
        except Exception as e:
            print("Couldn't load file", e)

    def save_file(self):
        code_editor = self.root.code_editor
        filepath = self.root.filepath.text

        try:
            with open(filepath, "w", encoding="utf8") as file:
                file.write(code_editor.text)
        except Exception as e:
            print("Couldn't save file", e)


MyApp().run()
