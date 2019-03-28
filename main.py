from kivy.app import App
from kivy.lang import Builder
from kivy.uix.codeinput import CodeInput
from kivy.extras.highlight import KivyLexer

KV = """
BoxLayout
    MyTextInput

<MyTextInput>:
    font_size: 24
    text: 'This is my text input'

"""

class MyTextInput(CodeInput):
    lexer=KivyLexer()

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        self.readonly = False
        if len(modifiers) and text:

            if modifiers[0] == "ctrl" and ord(text) in [270, 269, 43, 45, 61]:
                self.readonly = True

                if ord(text) in [270, 43]:
                    self.font_size += 1
                    self.cursor = (self.cursor[0] - 1, 0)
                    return
                if ord(text) in [269, 61, 45]:
                    self.font_size -= 1
                    self.cursor = (self.cursor[0] - 1, 0)
                    return

        return super(MyTextInput, self).keyboard_on_key_down(window, keycode, text, modifiers)


class MyApp(App):
    def build(self):
        self.root = Builder.load_string(KV)


MyApp().run()
