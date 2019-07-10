from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from kivymd.theming import ThemeManager
from kivymd.list import MDList, OneLineListItem
from kivymd.toast.kivytoast import toast



# нижние кнопки навигации
class BottomNavigationButton(AnchorLayout):
    icon = 'plus'

    def __init__(self, press_function):
        super().__init__()
        self.press_function = press_function
        return

class RightArrow(BottomNavigationButton):
    icon = 'arrow-right'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'right'
        return

class LeftArrow(BottomNavigationButton):
    icon = 'arrow-left'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'left'
        return

class Plus(BottomNavigationButton):
    icon = 'plus'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'center'
        return

# страница "О нас"
class AboutUsPage(AnchorLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        return

# страница "Инструкция"
class InstructionPage(AnchorLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        return

# верхнее панель меню
class MenuPanel(AnchorLayout):
    ___menu_item_names = ('Главная страница', 'Инструкция', 'О нас')

    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        self.menu_items = [{'viewclass': 'MDMenuItem',
                            'text': self.___menu_item_names[0],
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': self.___menu_item_names[1],
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': self.___menu_item_names[2],
                            'callback': self.callback_for_menu_items}]
        return

    def callback_for_menu_items(self, *args):
        if(args[0] == self.___menu_item_names[0]):
            self.MainLayout.new_page("StartPage")
        elif(args[0] == self.___menu_item_names[1]):
            self.MainLayout.new_page("InstructionPage")
        else:
            self.MainLayout.new_page("AboutUsPage")

# стартовая страница
class StartPage(BoxLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        return

    def btn_new_press_function(self):
        self.MainLayout.new_page("NewNamePage")
        return

    def btn_old_press_function(self):
        self.MainLayout.new_page("OldProjectsPage")
        return

# элемент списка существующих проектов
class ListItem(OneLineListItem):
    def __init__(self, text):
        super().__init__(text=text)
        return

# страница со списком существующих проектов
class OldProjectsPage(AnchorLayout):
    ListOfProjects = ["1 item", "2 item", '3 item']

    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        AL = AnchorLayout(anchor_x='center',
                          anchor_y='top',
                          size_hint=(1., 1.))
        MDL = MDList()
        for name in self.ListOfProjects:
            MDL.add_widget(ListItem(text=name))
        AL.add_widget(MDL)
        self.add_widget(AL)
        return

# страница введения названия нового проекта
class NewNamePage(AnchorLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        self.add_widget(RightArrow(self.right_arrow_press_function))
        return

    def right_arrow_press_function(self):
        self.MainLayout.new_page("ProjectPhotosPage")
        return

# страница добавления фотографий в новый проект
class ProjectPhotosPage(AnchorLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        self.add_widget(LeftArrow(self.left_arrow_press_function))
        self.add_widget(Plus(self.plus_press_function))
        self.add_widget(RightArrow(self.right_arrow_press_function))
        return

    def left_arrow_press_function(self):
        self.MainLayout.new_page("NewNamePage")
        return

    def plus_press_function(self):
        pass

    def right_arrow_press_function(self):
        pass


# главный слой
class MainLayout(AnchorLayout):
    current_page = None
    menu_panel = None
    pages = {
        "StartPage": None,
        "NewNamePage": None,
        "OldProjectsPage": None,
        "ProjectPhotosPage": None,
        "InstructionPage": None,
        "AboutUsPage": None
    }

    # инициализация
    def __init__(self):
        super().__init__(anchor_x='center', anchor_y='center')
        # нициализация дочерних объектов
        self.pages["StartPage"] = StartPage(self)
        self.pages["NewNamePage"] = NewNamePage(self)
        self.pages["OldProjectsPage"] = OldProjectsPage(self)
        self.pages["ProjectPhotosPage"] = ProjectPhotosPage(self)
        self.pages["InstructionPage"] = InstructionPage(self)
        self.pages["AboutUsPage"] = AboutUsPage(self)
        # добавление панели управления
        self.menu_panel = MenuPanel(self)
        self.add_widget(self.menu_panel)
        # открытие стартовой страницы
        self.new_page("StartPage")
        return

    def clear(self):
        try:
            self.remove_widget(self.current_page)
        except AttributeError:
            pass
        return

    def new_page(self, page):
        self.clear()
        self.current_page = self.pages[page]
        self.add_widget(self.current_page)



class MainApp(App):
    STATIC_PATH = "./static"
    SRC_PATH = "./src"

    theme_cls = ThemeManager()
    title = "My App"

    def build(self):
        self.theme_cls.theme_style = 'Light'

        return MainLayout()

