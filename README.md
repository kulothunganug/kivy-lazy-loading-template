# Kivy Lazy Loading - Template
Improve your kivy app's performance 🚀 by lazy loading.

This template will be very useful if your kivy app uses more screen,
In normal the app loads all the screens at once, it take some time to load all of it, if the screens contain much complex widgets, then it affects the start-up time.
To get rid of these issues, this template comes in.
When using this template the screen will only be loaded when you switching the screen, so the startup time reduces.

## Things you should know before using:
* Just loads the screen when `screen_manager_instance.set_current("name")` called and the arg should be avail in [screens.json](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/screens.json) as a key.
* Don't worry about loading the kv file it will automatically load when the screen enters.
* This template also supports to *go previous screen* when user press the back button (mobile) or ESC button (desktop), You can use `screen_manager_instance.goback()` to go the previous screen.
* All screen's py files should be in **libs/uix/baseclass** folder and their kv files in **libs/uix/kv**.
* For more info refer [libs/uix/root.py](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/libs/uix/root.py) and [screens.json](https://github.com/Kulothungan16/kivy-lazy-loading-template/blob/main/screens.json) to get a clearer view about this template.

## Goback to previous screen
* You should use `screen_manager_instance.goback()` when you want to go back to the previous screen, instead of `screen_manager_instance.set_current('prev_screen', side='right')` otherwise the history of the screen manager will be collapsed.


##### This template already contains two screens as example.