from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from .Pages import ProjectPhotosPage, OldProjectsPage



Builder.load_string("""
#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton

<StartPage>:
    orientation: 'vertical'
    size_hint: (.7, .3)
    spacing: 50

    MDFillRoundFlatButton:
        text: 'Создать новый'
        size_hint: (1., 1.)
        on_press: root.btn_new_press_function()

    MDFillRoundFlatButton:
        text: 'Открыть старый'
        size_hint: (1., 1.)
        on_press: root.btn_old_press_function()
""")


# стартовая страница
class StartPage(BoxLayout):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        return

    def btn_new_press_function(self):
        self.layout.new_page(ProjectPhotosPage(self.layout))
        return

    def btn_old_press_function(self):
        self.layout.new_page(OldProjectsPage(self.layout))
        return


Builder.load_string("""
#:import MDLabel kivymd.uix.label.MDLabel

<AboutUsPage>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: (.8, .8)

    MDLabel:
        id: about_us_label
        text: "О нас"
        font_style: 'Subtitle1'
        theme_text_color: 'Primary'
        markup: True
        halign: 'center'
""")

# страница "О нас"
class AboutUsPage(AnchorLayout):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        return



Builder.load_string("""
#:import MDLabel kivymd.uix.label.MDLabel

<InstructionPage>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: (.8, .8)

    MDLabel:
        text: "Инструкция"
        font_style: 'Subtitle1'
        theme_text_color: 'Primary'
        markup: True
        halign: 'center'
""")

# страница "Инструкция"
class InstructionPage(AnchorLayout):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        return