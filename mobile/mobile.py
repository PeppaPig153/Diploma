import os

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

from kivymd.list import MDList, OneLineListItem
from kivymd.toast.kivytoast import toast
from kivymd.utils.cropimage import crop_image
from kivymd.imagelists import SmartTile


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
        self.MainLayout.new_page("ProjectNamePage")
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
    ListOfProjects = ["1 item", "2 item", "3 item", "4 item", "5 item", "6 item", "7 item", "8 item", "9 item",
                      "10 item", "11 item", "12 item", "13 item", "14 item", "15 item"]

    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout  # главный слой
        for name in self.ListOfProjects:
            self.ids["MDL"].add_widget(ListItem(text=name))
        return

# страница введения названия нового проекта
class ProjectNamePage(AnchorLayout):
    def __init__(self, MainLayout):
        super().__init__()
        self.MainLayout = MainLayout # главный слой
        self.add_widget(RightArrow(self.right_arrow_press_function))
        return

    def right_arrow_press_function(self):
        self.MainLayout.new_page("ProjectPhotosPage")
        return


class TileImage(SmartTile):
    def __init__(self, path_to_crop_image):
        super().__init__()
        try:
            self.crop_image_for_tile([20, 20], path_to_crop_image)
        except Exception as err:
            print(err)

    def crop_image_for_tile(self, size, path_to_crop_image):
        if not os.path.exists(os.path.join(self.directory, path_to_crop_image)):
            size = (int(size[0]), int(size[1]))
            path_to_origin_image = path_to_crop_image.replace("_tile_crop", "")
            crop_image(size, path_to_origin_image, path_to_crop_image)
        self.source = path_to_crop_image


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
        self.MainLayout.new_page("ProjectNamePage")
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
        "ProjectNamePage": None,
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
        self.pages["ProjectNamePage"] = ProjectNamePage(self)
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





