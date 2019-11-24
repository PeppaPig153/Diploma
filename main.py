from mobile.mobile import MainLayout
from kivy.app import App
from kivymd.theming import ThemeManager


class MainApp(App):
    STATIC_PATH = "./static"
    SRC_PATH = "./src"

    theme_cls = ThemeManager()
    title = "My App"

    def build(self):
        self.theme_cls.theme_style = 'Light'

        return MainLayout()

if __name__ == "__main__":
    MainApp().run()