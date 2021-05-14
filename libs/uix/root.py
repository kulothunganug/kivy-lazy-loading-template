from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager


class Root(ScreenManager):

    previous_screen = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._goto_previous_screen)

    def set_current(self, screen_name, side="left"):
        # checks that the screen already added to the screen-manager
        if not self.has_screen(screen_name):
            # loads the kv file
            Builder.load_file(
                f"libs/uix/kv/{screen_name}_screen.kv",
            )
            # imports the screen class dynamically
            exec(
                f"from baseclass.{screen_name}_screen import {screen_name.title()}Screen"
            )
            # calls the screen class to get the instance of it
            screen_object = eval(f"{screen_name.title()}Screen()")
            # automatically sets the screen name using the arg that passed in set_current
            screen_object.name = screen_name
            # finnaly adds the screen to the screen-manager
            self.add_widget(screen_object)

        # saves previous screen information
        self.previous_screen = {"name": self.current, "side": side}
        # sets transition direction
        self.transition.direction = side
        # sets to the current screen
        self.current = screen_name

    def _goto_previous_screen(self, instance, key, *args):
        if key == 27 and self.previous_screen:
            self.goto_previous_screen()
            return True

    def goto_previous_screen(self):
        self.set_current(
            self.previous_screen["name"],
            side="right" if self.previous_screen["side"] == "left" else "left",
        )
