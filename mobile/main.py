from kivy.app import App
from kivymd.theming import ThemeManager
from mobile import MainLayout

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