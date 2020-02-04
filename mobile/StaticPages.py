from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

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