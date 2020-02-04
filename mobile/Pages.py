from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.factory import Factory
from kivy.lang import Builder


from .BottomNavigationButtons import RightArrow, LeftArrow, Plus, Shoot


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
        self.layout.new_page(ProjectNamePage(self.layout))
        return

    def btn_old_press_function(self):
        self.layout.new_page(OldProjectsPage(self.layout))
        return

########################################################################################################################

Builder.load_string("""
#:import MDTextField kivymd.uix.textfield.MDTextField

<ProjectNamePage>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: (1., 1.)

    MDTextField:
        hint_text: "Название проекта"
        max_text_length: 30
        #required: True
        size_hint: (.7, .1)
""")

# страница введения названия нового проекта
class ProjectNamePage(AnchorLayout):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        self.add_widget(RightArrow(self.right_arrow_press_function))
        return

    def right_arrow_press_function(self):
        self.layout.new_page(ProjectPhotosPage(self.layout))
        return

########################################################################################################################

Builder.load_string("""
<ListItem@OneLineListItem>:
    MDIconButton:
        icon: 'close'
        pos_hint: {'top': 1, 'right': 1}

<ScrollList>:
    orientation: "vertical"
    size_hint: (1., 1.)

    ScrollView:
        MDList:
            id: scroll

<OldProjectsPage>:
    anchor_x: 'center'
    anchor_y: 'bottom'
    size_hint: (1., 1.)
""")


class ScrollList(BoxLayout):
    pass


# страница со списком существующих проектов
class OldProjectsPage(AnchorLayout):
    ListOfProjects = ["1 item", "2 item", "3 item", "4 item", "5 item", "6 item", "7 item", "8 item", "9 item",
                      "10 item", "11 item", "12 item", "13 item", "14 item", "15 item"]

    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        self.list = ScrollList()
        for name in self.ListOfProjects:
            self.list.ids["scroll"].add_widget(Factory.ListItem(text=name))
        self.add_widget(self.list)
        return

########################################################################################################################

Builder.load_string("""
<ProjectPhotosPage>:
    anchor_x: 'center'
    anchor_y: 'bottom'
    size_hint: (1., 1.)

    #AnchorLayout:
    #    id: panel
    #    anchor_x: 'center'
    #    anchor_y: 'bottom'
    #    size_hint: (1., .3)

    AnchorLayout:
        id: photos
        anchor_x: 'center'
        anchor_y: 'bottom'
        size_hint: (1., .8)

        ScrollView:
            do_scroll_x: True

            GridLayout:
                cols: 2
                size_hint: (1., 1.)
""")


# страница добавления фотографий в новый проект
class ProjectPhotosPage(AnchorLayout):
    def __init__(self, layout):
        super().__init__()
        self.layout = layout  # главный слой
        self.add_widget(LeftArrow(self.left_arrow_press_function))
        self.add_widget(Plus(self.plus_press_function))
        self.add_widget(RightArrow(self.right_arrow_press_function))
        return

    def left_arrow_press_function(self):
        self.layout.new_page(ProjectNamePage(self.layout))

    def plus_press_function(self):
        self.layout.new_page(CameraPage(self.layout))

    def right_arrow_press_function(self):
        pass

########################################################################################################################

Builder.load_string("""
#:import Window kivy.core.window.Window

<CameraPage>:
    anchor_x: 'center'
    anchor_y: 'center'
    size_hint: (1., 1.)

    Camera:
        id: camera
        resolution: Window.size
        play: True
""")


class CameraPage(AnchorLayout):
    def __init__(self, layout):
        super().__init__()
        self.add_widget(Shoot(self.capture))
        self.layout = layout  # главный слой
        # sizes = camera.image_sizes()
        # appuifw.app.orientation = 'landscape'
        # canvas = appuifw.Canvas()

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        # camera = self.ids['camera']
        # timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")