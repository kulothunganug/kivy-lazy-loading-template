import json

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager

from libs.applibs import utils


class Root(ScreenManager):

    history = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._handle_keyboard)
        # getting screens data from screens.json
        with open(utils.abs_path("screens.json")) as f:
            self.screens_data = json.load(f)

    def set_current(self, screen_name, side="left", _from_goback=False):
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_file.py in libs/uix/baseclass/
            2. Create screen_file.kv in libs/uix/kv/
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "screen_name": {
                        "import": "from libs.uix.baseclass.screen_py_file import ScreenObjectName",
                        "object": "ScreenObjectName()",
                        "kv": "libs/uix/kv/screen_kv_file.kv"
                    }
                }

                Note: In .JSON you must not use:
                        * Unneeded Commas
                        * Comments
        """

        # checks that the screen already added to the screen-manager
        if not self.has_screen(screen_name):
            screen = self.screens_data[screen_name]
            # loads the kv file
            Builder.load_file(utils.abs_path(screen["kv"]))
            # imports the screen class dynamically
            exec(screen["import"])
            # calls the screen class to get the instance of it
            screen_object = eval(screen["object"])
            # automatically sets the screen name using the arg that passed in set_current
            screen_object.name = screen_name
            # finnaly adds the screen to the screen-manager
            self.add_widget(screen_object)

        # saves screen information to history
        # if you not want a screen to go back
        # use like below
        # if not from_goback and screen_name not in ["auth", ...]
        if not _from_goback:
            self.history.append({"name": screen_name, "side": side})

        # sets transition direction
        self.transition.direction = side
        # sets to the current screen
        self.current = screen_name

    def _handle_keyboard(self, instance, key, *args):
        if key == 27:
            self.goback()
            return True

    def goback(self):
        if len(self.history) > 1:
            prev_side = self.history.pop()["side"]
            prev_screen = self.history[-1]

            if prev_side == "left":
                side = "right"
            elif prev_side == "right":
                side = "left"
            elif prev_side == "up":
                side = "down"
            elif prev_side == "down":
                side = "up"

            self.set_current(prev_screen["name"], side=side, _from_goback=True)
