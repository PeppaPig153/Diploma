import os
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.theming import ThemeManager
from kivymd.list import MDList, OneLineListItem

class MenuPanel(AnchorLayout):
    def __init__(self):
        super().__init__()
        return


class StartPage(BoxLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout
        return

    def btn_new_press_function(self):
        print("new")
        return

    def btn_old_press_function(self):
        self.MainLayout.clear()
        self.MainLayout.add_widget(OldProjectsPage())
        return


class OldProjectsPage(FloatLayout):
    ListOfProjects = ["1 item", "2 item", '3 item']
    def __init__(self):
        super().__init__()
        AL = AnchorLayout(anchor_x='center',
                          anchor_y='top',
                          size_hint=(1., 1.))
        MDL = MDList()
        for name in self.ListOfProjects:
            MDL.add_widget(OneLineListItem(text=name))
        AL.add_widget(MDL)
        self.add_widget(AL)
        return


# главный слой
class MainLayout(AnchorLayout):
    page = None

    # инициализация
    def __init__(self):
        super().__init__(anchor_x='center', anchor_y='center')
        self.add_widget(MenuPanel())
        self.start()
        return

    def clear(self):
        try:
            self.remove_widget(self.page)
        except AttributeError:
            pass
        return

    # стартовая страница
    def start(self):
        self.clear()
        self.page = StartPage(self)
        self.add_widget(self.page)
        return self

    # функции кнопок
    def btn_new_press(self):
        print("new")
        return

    def btn_old_press(self):
        print("old")
        return


class MainApp(App):
    STATIC_PATH = "./static"
    SRC_PATH = "./src"

    theme_cls = ThemeManager()
    title = "My App"

    def build(self):
        self.theme_cls.theme_style = 'Light'

        return MainLayout()

