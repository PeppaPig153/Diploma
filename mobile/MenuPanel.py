from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

from .Pages import StartPage
from .StaticPages import InstructionPage, AboutUsPage

from kivymd.uix.menu import MDDropdownMenu


Builder.load_string("""
#:import MDToolbar kivymd.uix.toolbar.MDToolbar
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu

<MenuPanel>:
    anchor_x: 'center'
    anchor_y: 'top'
    size_hint: (1., 1.)

    MDToolbar:
        title: 'Меню'
        md_bg_color: app.theme_cls.primary_color
        right_action_items: [['dots-vertical', lambda x: MDDropdownMenu(items=root.menu_items, width_mult=3).open(self)]]


""")


# верхнее панель меню
class MenuPanel(AnchorLayout):
    menu_item_names = ('Главная страница', 'Инструкция', 'О нас')

    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        self.menu_items = [{'viewclass': 'MDMenuItem',
                            'text': self.menu_item_names[0],
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': self.menu_item_names[1],
                            'callback': self.callback_for_menu_items},
                           {'viewclass': 'MDMenuItem',
                            'text': self.menu_item_names[2],
                            'callback': self.callback_for_menu_items}]
        return

    def callback_for_menu_items(self, *args):
        if (args[0] == self.menu_item_names[0]):
            self.layout.new_page(StartPage(self.layout))
        elif (args[0] == self.menu_item_names[1]):
            self.layout.new_page(InstructionPage(self.layout))
        else:
            self.layout.new_page(AboutUsPage(self.layout))