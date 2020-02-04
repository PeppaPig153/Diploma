from kivy.uix.anchorlayout import AnchorLayout

from .Pages import StartPage
from .MenuPanel import MenuPanel


class MainLayout(AnchorLayout):
    def __init__(self):
        super().__init__(anchor_x='center', anchor_y='bottom')
        self.layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint=(1.0, 0.9))
        self.add_widget(self.layout)
        self.menu_panel = MenuPanel(self)
        self.add_widget(self.menu_panel)
        self.new_page(StartPage(self))
        return


    def new_page(self, new_page):
        self.layout.clear_widgets()
        self.layout.add_widget(new_page)