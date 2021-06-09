# Kivy Lazy Loading - Template
Improve your kivy app's performance 🚀 by lazy loading.

## Things you should know before using:
* Just loads the screen when `screen_manager_instance.set_current("name")` called and the arg should be avail in [screens.json](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/screens.json) as a key.
* This template also supports to *go previous screen* when user press the back button (mobile) or ESC button (desktop), You can also use `screen_manager_instance.goto_previous_screen()` to go the previous screen.
* Don't worry about loading the kv file it will automatically load when the screen enters.
* This template already contains two screens as example.
* All screen's py files should be in *libs/uix/baseclass* folder and their kv files in *libs/uix/kv*.
* For more info refer [*libs/uix/root.py*](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/libs/uix/root.py) and [screens.json](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/screens.json) to get a clearer view about this template.
