from mobile.MainLayout import MainLayout
from kivymd.app import MDApp
from kivymd.theming import ThemeManager


class MainApp(MDApp):
    STATIC_PATH = "./static"
    SRC_PATH = "./src"

    def __init__(self, **kwargs):
        self.title = "My App"
        self.theme_cls = ThemeManager()
        super().__init__(**kwargs)

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'LightBlue'
        return MainLayout()

if __name__ == "__main__":
    MainApp().run()