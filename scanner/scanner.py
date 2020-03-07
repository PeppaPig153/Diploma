import cv2 as cv
import numpy as np
import math


def findSquare(contours):
    area_difference = [cv.contourArea(cv.boxPoints(cv.minAreaRect(contour))) - cv.contourArea(contour) for contour in contours]
    side_difference = []
    for i in range(len(area_difference)):
        if area_difference[i] < 10:
            square = cv.boxPoints(cv.minAreaRect(contours[i]))
            sides = [square[j] - square[(j+1)%4] for j in range(4)]
            sides_length = [math.hypot(side[0], side[1]) for side in sides]
            side_difference.append((i, max(sides_length)-min(sides_length)))
    return min(side_difference, key = lambda contour: contour[1])[0]


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


def scanner_video():
    continue_cycle = True
    cap = cv.VideoCapture(0) # захват видеопотока, аргумент - номер камеры или название видеофайла

    while (continue_cycle):
        _, frame = cap.read() # получение кадра

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


        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)
        # отображаем контуры поверх изображения
        cv.drawContours(frame, contours, -1, CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)
        cv.drawContours(result, contours, -1, CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)

        # отображение полученных результатов
        cv.namedWindow('Original', cv.WINDOW_AUTOSIZE)
        cv.imshow('Original', frame)
        cv.namedWindow('Result', cv.WINDOW_AUTOSIZE)
        cv.imshow('Result', result)


        k = (cv.waitKey(5) & 0xFF) # выход по ESC
        if k == 27:
            continue_cycle = False

    cv.destroyAllWindows()
    cap.release()

def scanner_image(filename=""):
    continue_cycle = True

    while (continue_cycle):
        frame = cv.imread(filename) # получение кадра

        # опеределение новых размеров изображения
        h, w, _ = frame.shape
        dim = (int(w * HEIGHT / h), HEIGHT) if (h > w) else (WIDTH, int(h * WIDTH / w))
        frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)

        # вот это нужно проверить
        # image – Source, an 8 - bit single - channel image. Non - zero pixels are treated as 1’s.Zero pixels
        # remain 0’s, so the image is treated as binary.You can use
        # compare(), inRange(), threshold(), adaptiveThreshold(), Canny(), and othersto create a binary image out
        # of a grayscale or color one.The function  modifies the image while extracting the contours.
        # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # изменение цветовой схемы
        # src_gray = cv.blur(hsv, (3, 3))
        # cv.threshold(image, image, 128, 255, CV_THRESH_BINARY);
        # mask = cv.inRange(hsv, lower_level, upper_level)  # накладывае на кадр цветовой фильтр в заданном диапазоне
        # res = cv.bitwise_and(frame, frame, mask=mask)  # вычисляет битовое соединение двух массивов или массива и скаляра

        result = cv.Canny(frame, 100, 200, 1)  # детектор границ Кенни

        # ищем контуры и складируем их в переменную contours
        contours, hierarchy = cv.findContours(result, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        square_index = findSquare(contours)
        # square = contours.pop(square_index)
        # hierarchy = np.array([np.delete(hierarchy[0], square_index, axis=0)])

        areas = [cv.contourArea(contour) for contour in contours]  # вычисление площади каждого контура
        areas[square_index] = 0
        result = cv.cvtColor(result, cv.COLOR_BGR2BGRA)
        # отображаем контуры поверх изображения
        cv.drawContours(frame, contours, -1, CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)
        cv.drawContours(result, contours, areas.index(max(areas)), CONTOUR_COLOR, THICKNESS, cv.LINE_AA, hierarchy, 1)
        cv.drawContours(result, contours, square_index, (0, 255, 0), THICKNESS, cv.LINE_AA, hierarchy, 1)

        # отображение полученных результатов
        cv.namedWindow('Original', cv.WINDOW_AUTOSIZE)
        cv.imshow('Original', frame)
        cv.namedWindow('Result', cv.WINDOW_AUTOSIZE)
        cv.imshow('Result', result)

        f = open('path.svg', 'w+')
        f.write('<svg width="' + str(w//2) + '" height="' + str(h//2) + '" xmlns="http://www.w3.org/2000/svg">')


        for contour in contours:
            if cv.contourArea(contour) > 10:
                f.write('<path d="M ')
                for i in range(len(contour)):
                    x, y = contour[i][0]
                    f.write(str(x) + ' ' + str(y) + ' ')
                f.write('"/>')

        f.write('</svg>')
        f.close()


        k = cv.waitKey(0)  # выход по ESC
        if k == 27:
            continue_cycle = False

    cv.destroyAllWindows()


if __name__=='__main__':
    # scanner_video()
    # scanner_image("../src/prob.jpg")
    scanner_image("../src/test.jpg")
   #  scanner_image("../src/bubl.jpg")



# findContours( кадр, режим_группировки, метод_упаковки [, контуры[, иерархия[, сдвиг]]])
# кадр — должным образом подготовленная для анализа картинка. Это должно быть 8-битное изображение. Поиск контуров использует для работы монохромное изображение, так что все пиксели картинки с ненулевым цветом будут интерпретироваться как 1, а все нулевые останутся нулями. На уроке про поиск цветных объектов была точно такая же ситуация. режим_группировки — один из четырех режимов группировки найденных контуров:
#    CV_RETR_LIST — выдаёт все контуры без группировки;
#    CV_RETR_EXTERNAL — выдаёт только крайние внешние контуры. Например, если в кадре будет пончик, то функция вернет его внешнюю границу без дырки.
#    CV_RETR_CCOMP — группирует контуры в двухуровневую иерархию. На верхнем уровне — внешние контуры объекта. На втором уровне — контуры отверстий, если таковые имеются. Все остальные контуры попадают на верхний уровень.
#    CV_RETR_TREE — группирует контуры в многоуровневую иерархию.
# метод_упаковки — один из трёх методов упаковки контуров:
#    CV_CHAIN_APPROX_NONE — упаковка отсутствует и все контуры хранятся в виде отрезков, состоящих из двух пикселей.
#    CV_CHAIN_APPROX_SIMPLE — склеивает все горизонтальные, вертикальные и диагональные контуры.
#    CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS — применяет к контурам метод упаковки (аппроксимации) Teh-Chin.
# контуры — список всех найденных контуров, представленных в виде векторов; иерархия — информация о топологии контуров. Каждый элемент иерархии представляет собой сборку из четырех индексов, которая соответствует контуру[i]:
# иерархия[i][0] — индекс следующего контура на текущем слое;
# иерархия[i][1] — индекс предыдущего контура на текущем слое:
# иерархия[i][2] — индекс первого контура на вложенном слое;
# иерархия[i][3] — индекс родительского контура.
# сдвиг — величина смещения точек контура.

# cv.contourArea(cnt) - вычисление площади контура

# Экстремальные точки:
# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
# topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

# Иерархия:
# [Next, Previous, First_Child, Parent]

# cvCanny(image, edges, threshold1, threshold2, aperture_size CV_DEFAULT(3))
# image — одноканальное изображение для обработки (градации серого)
# edges — одноканальное изображение для хранения границ, найденных функцией
# threshold1 — порог минимума
# threshold2 — порог максимума
# aperture_size — размер для оператора Собеля

# glScale - масштабирование контуров

