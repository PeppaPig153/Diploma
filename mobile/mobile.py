from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.config import Config
from kivy.core.window import Window

class AppButton(Button):
    def __init__(self, text, btn_press_function):
        self.BUTTONS_COLOR = [130, 58, 0, 1]
        super().__init__(text=text,
                         background_color=self.BUTTONS_COLOR,
                         on_press=btn_press_function)

class BackgroundImage:
    def __init__(self, filename):
        self.bg_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        self.bg_picture = AsyncImage(source=filename,
                                     allow_stretch=True)
        self.bg_layout.add_widget(self.bg_picture)


class MainApp(App):
    def build(self):
        # удалить
        # k = 60
        # Config.set('graphics', 'width', 6 * k)
        # Config.set('graphics', 'height', 11 * k)

        self.BACKGROUND_COLOR = [0, 0, 205, 1] # цвет фона в формате RGBA
        self.main_layout = AnchorLayout() # создаём слой, на котором всё будет расположено
        self.start_page() # начинаем со стартовой страницы
        return self.main_layout


    def main_layout_init(self):
        self.main_layout.clear_widgets() # очищаем
        # красим главный слой
        with self.main_layout.canvas.before:
            Color(*self.BACKGROUND_COLOR)
            self.rect = Rectangle(size=self.main_layout.size, pos=self.main_layout.pos)

        self.main_layout.bind(size=self._update_rect, pos=self._update_rect)
        return


    def start_page(self):
        self.main_layout_init() # подготавливаем основной слой
        # кнопки
        button_new = AppButton("Создать новую", self.bth_new_press)
        button_old = AppButton("Выбрать существующую", self.bth_old_press)

        # слой кнопок
        buttons_layout = BoxLayout(orientation='vertical',
                                   size_hint=(.7, .4),
                                   spacing=50)

        # добавляем кнопки
        buttons_layout.add_widget(button_new)
        buttons_layout.add_widget(button_old)

        # добавляем фон на основной слой
        self.main_layout.add_widget(BackgroundImage("../source/main_page_bg.png").bg_layout)

        # добавляем слой кнопок на основной слой
        self.main_layout.add_widget(buttons_layout)
        return


    def choose_photo_page(self):
        self.main_layout_init()  # подготавливаем основной слой
        # кнопки
        button_choose_photo = AppButton("Выбрать фотографию", self.bth_choose_photo_press)

        # слой кнопок
        buttons_layout = BoxLayout(orientation='vertical',
                                   size_hint=(.7, .2),
                                   spacing=50)
        # добавляем кнопки
        buttons_layout.add_widget(button_choose_photo)

        # добавляем фон на основной слой
        self.main_layout.add_widget(BackgroundImage("../source/choose_photo_page_bg.png").bg_layout)

        # добавляем слой кнопок на основной слой
        self.main_layout.add_widget(buttons_layout)
        return



    # обновление размеров фона
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        return



    # функции нажатия кнопок
    def bth_new_press(self, instance):
        self.choose_photo_page()
        return


    def bth_old_press(self, instance):
        print('Старая')
        return


    def bth_choose_photo_press(self, instance):
        print('Выбрать фото')
        return
