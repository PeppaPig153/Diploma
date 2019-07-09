from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemeManager
from kivymd.list import MDList, OneLineListItem
from kivymd.toast.kivytoast import toast


class MenuPanel(AnchorLayout):
    def __init__(self):
        super().__init__()
        self.menu_items = [{'viewclass': 'MDMenuItem',
                            'text': 'Главная страница',
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': 'Помощь',
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': 'О нас',
                            'callback': self.callback_for_menu_items}]
        return

    def callback_for_menu_items(self, *args):
        toast(args[0])


class StartPage(BoxLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout
        return

    def btn_new_press_function(self):
        self.MainLayout.clear()
        self.MainLayout.page = NewNamePage()
        self.MainLayout.add_widget(self.MainLayout.page)
        return

    def btn_old_press_function(self):
        self.MainLayout.clear()
        self.MainLayout.page = OldProjectsPage()
        self.MainLayout.add_widget(self.MainLayout.page)
        return


class ListItem(OneLineListItem):
    def __init__(self, text):
        super().__init__(text=text)
        return


class OldProjectsPage(AnchorLayout):
    ListOfProjects = ["1 item", "2 item", '3 item']
    def __init__(self):
        super().__init__()
        AL = AnchorLayout(anchor_x='center',
                          anchor_y='top',
                          size_hint=(1., 1.))
        MDL = MDList()
        for name in self.ListOfProjects:
            MDL.add_widget(ListItem(text=name))
        AL.add_widget(MDL)
        self.add_widget(AL)
        return


class NewNamePage(AnchorLayout):
    def __init__(self):
        super().__init__()
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

