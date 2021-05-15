from kivy.app import App
from kivy.core.window import Window

from libs.uix.root import Root


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "Kivy - Lazy Load"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()
        self.root.set_current("home")


if __name__ == "__main__":
    MainApp().run()
