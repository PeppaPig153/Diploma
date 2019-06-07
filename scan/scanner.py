import cv2 as cv
import numpy as np

# параметры цветового фильтра
lower_level = np.array([30, 150, 50])
upper_level = np.array([255, 255, 180])
WIDTH, HEIGHT = 100, 200

def scanner(filename = ""):
    continue_cycle = True
    from_video = (filename == "")
    cap = cv.VideoCapture(0) if from_video else None # захват видеопотока, аргумент - номер камеры или название видеофайла

    while (continue_cycle):
        _, frame = cap.read() if from_video else (None, cv.imread(filename)) # получение кадра

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) # изменение цветовой схемы

        mask = cv.inRange(hsv, lower_level, upper_level) # накладывае на кадр цветовой фильтр в заданном диапазоне

        res = cv.bitwise_and(frame, frame, mask=mask) # вычисляет битовое соединение двух массивов или массива и скаляра
                                                      # для каждого элемента

        cv.imshow('Original', frame) # отображение оригинального изображения
        cv.resizeWindow('Original', WIDTH, HEIGHT)

        edges = cv.Canny(frame, 100, 200) # детектор границ Кенни

        cv.imshow('Result', edges) # отображает полученное изображение


        k = (cv.waitKey(5) & 0xFF) if from_video else cv.waitKey(0) # выход по ESC
        if k == 27:
            continue_cycle = False

    cv.destroyAllWindows()
    if(from_video):
        cap.release()