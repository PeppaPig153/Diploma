from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout


Builder.load_string("""
#:import MDFloatingActionButton kivymd.uix.button.MDFloatingActionButton

<BottomRoundButton>:
    anchor_x: 'left'
    anchor_y: 'bottom'
    size_hint: (1., 1.)
    padding: 20

    MDFloatingActionButton:
        icon: root.icon
        opposite_colors: True
        elevation_normal: 8
        md_bg_color: app.theme_cls.primary_color
        on_press: root.press_function()
""")


# нижние кнопки навигации
class BottomRoundButton(AnchorLayout):
    icon = 'plus'

    def __init__(self, press_function):
        super().__init__()
        self.press_function = press_function
        return


class RightArrow(BottomRoundButton):
    icon = 'arrow-right'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'right'
        return


class LeftArrow(BottomRoundButton):
    icon = 'arrow-left'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'left'
        return


class Plus(BottomRoundButton):
    icon = 'plus'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'center'
        return


class Shoot(BottomRoundButton):
    icon = 'camera'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'center'
        return


Builder.load_string("""
#:import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton

<BottomRectangleButton>:
    anchor_x: 'left'
    anchor_y: 'bottom'
    size_hint: (1., 1.)
    padding: 20
    
    MDRectangleFlatButton:
        text: root.text
        #opposite_colors: True
        elevation_normal: 8
        #md_bg_color: app.theme_cls.primary_color
        on_press: root.press_function()
""")


class BottomRectangleButton(AnchorLayout):
    icon = 'plus'

    def __init__(self, press_function):
        super().__init__()
        self.press_function = press_function
        return

class OK(BottomRectangleButton):
    text = 'Ok'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'right'
        return

class Cancel(BottomRectangleButton):
    text = 'Cancel'

    def __init__(self, press_function):
        super().__init__(press_function)
        self.anchor_x = 'left'
        return


