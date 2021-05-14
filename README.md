# Kivy Lazy Loading - Template
Improves your kivy app's performance 🚀 by lazy loading.

## Things you should know before using:
* Just loads the screen when `screen_manager_instance.set_current("name")` called and the arg should be in lowercase.
* This template also supports to go previous screen when user press the back button (mobile) or ESC button (desktop), You can also use`screen_manager_instance.goto_previous_screen()` to go the previous screen.
* Don't worry about loading the kv file it will automatically load when the screen enters.
* Screen name will be set automatically according to the arg passed in `screen_manager_instance.set_current`.
* For example this template already contains two screens.
* All screen py files should be in *libs/uix/baseclass* folder and their kv files in *libs/uix/kv*.
* Screen's files name should looks like this `name_screen.py` and `name_screen.kv`.
* Their class should needs to be looks like this `class NameScreen(Screen)` and they are case sensitive so you can't create another like this `class nameScreen(Screen)` that will throw error.
* For more info refer the [*libs/uix/root.py*](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/libs/uix/root.py) to get a clearer view about this template
