import cv2 as cv
import numpy as np

class Scanner:
    def __init__(self):
        # параметры цветового фильтр
        self.LOWER_LEVEL = np.array([30, 150, 50])
        self.UPPER_LEVEL = np.array([255, 255, 180])
        self.THICKNESS = 3 # толщина линии контура
        self.CONTOUR_COLOR = (255, 0, 0)

    def scan(self, filename=""):
        try:
            file = open(filename)
        except IOError:
            print('Unable to open file!')
        else:
            frame = cv.imread(filename)  # получение кадра
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # изменение цветовой схемы

            mask = cv.inRange(hsv, self.LOWER_LEVEL, self.UPPER_LEVEL) # накладывае на кадр цветовой фильтр в заданном диапазоне

            res = cv.bitwise_and(frame, frame, mask=mask) # вычисляет битовое соединение двух массивов или массива и скаляра
                                                          # для каждого элемента

            result = cv.Canny(frame, 100, 200, 1)  # детектор границ Кенни

            # ищем контуры и складируем их в переменную contours
            contours, hierarchy = cv.findContours(result, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)

            # попытка убрать маленькие контуры (для видео работает не очень)
            # try:
            #     counter = 0
            #     while (counter < len(contours)):
            #         if(contours[counter].shape[0] < 4):
            #             contours.pop(counter)
            #             hierarchy = np.delete(hierarchy, counter, axis = 1)
            #         else:
            #             counter += 1
            # except IndexError as err:
            #     print(err)

            cv.drawContours(frame, contours, -1, self.CONTOUR_COLOR, self.THICKNESS, cv.LINE_AA, hierarchy, 1)
            cv.imwrite(filename, frame)

            return contours



# параметры цветового фильтра
lower_level = np.array([30, 150, 50])
upper_level = np.array([255, 255, 180])
# размеры окна
WIDTH, HEIGHT = (600, 600) # сюда следует записывать размеры экрана устройства
# толщина линии контура
THICKNESS = 3
# цвет линии контура в формате BGR
CONTOUR_COLOR = (255, 0, 0)


def scanner(filename=""):
    continue_cycle = True
    from_video = (filename == "")
    cap = cv.VideoCapture(0) if from_video else None # захват видеопотока, аргумент - номер камеры или название видеофайла

    while (continue_cycle):
        _, frame = cap.read() if from_video else (None, cv.imread(filename)) # получение кадра

        # опеределение новых размеров изображения
        h, w, _ = frame.shape
        dim = (int(w * HEIGHT / h), HEIGHT) if (h > w) else (WIDTH, int(h * WIDTH / w))
        frame = cv.resize(frame, dim, interpolation = cv.INTER_AREA)

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # изменение цветовой схемы

        mask = cv.inRange(hsv, lower_level, upper_level) # накладывае на кадр цветовой фильтр в заданном диапазоне

        res = cv.bitwise_and(frame, frame, mask=mask) # вычисляет битовое соединение двух массивов или массива и скаляра
                                                      # для каждого элемента

        result = cv.Canny(frame, 100, 200, 1)  # детектор границ Кенни

        # ищем контуры и складируем их в переменную contours
        contours, hierarchy = cv.findContours(result, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)

        # попытка убрать маленькие контуры (для видео работает не очень)
        # try:
        #     counter = 0
        #     while (counter < len(contours)):
        #         if(contours[counter].shape[0] < 4):
        #             contours.pop(counter)
        #             hierarchy = np.delete(hierarchy, counter, axis = 1)
        #         else:
        #             counter += 1
        # except IndexError as err:
        #     print(err)

        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)
        # отображаем контуры поверх изображения
        cv.drawContours(frame, contours, -1, CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)
        cv.drawContours(result, contours, -1, CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)

        # отображение полученных результатов
        cv.namedWindow('Original', cv.WINDOW_AUTOSIZE)
        cv.imshow('Original', frame)
        cv.namedWindow('Result', cv.WINDOW_AUTOSIZE)
        cv.imshow('Result', result)


        k = (cv.waitKey(5) & 0xFF) if from_video else cv.waitKey(0) # выход по ESC
        if k == 27:
            continue_cycle = False

    cv.destroyAllWindows()
    if(from_video):
        cap.release()


if __name__=='__main__':
    scanner()