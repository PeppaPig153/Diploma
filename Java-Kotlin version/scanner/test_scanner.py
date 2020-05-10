import numpy as np
import cv2 as cv


# ГЛОБАЛЬНЫЕ ПАРАМЕТРЫ
window_names = ["48 MP", "13 MP", "8 MP"]  # названия для окон
trackbar_window_name = "Settings"  # название окна с трекбарами
THICKNESS = 4  # толщина линии контура
CONTOUR_COLOR = (0, 255, 0)
M = 3  # кол-во телефонов
P = 3  # кол-во фотографий
kx = [0.08, 0.08, 0.25]  # коэффициенты сокращения


# ПАРАМЕТРЫ FINDCONTOURS
mode = [  # режим группировки найденных контуров
    cv.RETR_LIST,  # все контуры без группировки
    cv.RETR_EXTERNAL,  # только крайние внешние контуры
    cv.RETR_CCOMP,  # контуры в двухуровневой иерархии
    cv.RETR_TREE   # контуры в многоуровневой иерархии
]
method = [  # метод упаковки контуров
    cv.CHAIN_APPROX_NONE,  # упаковка отсутствует и все контуры хранятся в виде отрезков, состоящих из двух пикселей
    cv.CHAIN_APPROX_SIMPLE,  # cклеивает все горизонтальные, вертикальные и диагональные контуры
    cv.CHAIN_APPROX_TC89_KCOS,  # применяет к контурам метод упаковки (аппроксимации) Teh-Chin
]

# ПАРАМЕТРЫ CANNY
canny_param_names = ["threshold1", "threshold2", "apertureSize"]
threshold1 = [100, 200]
threshold2 = [200, 400]
apertureSize = [0, 2]


# ПАРАМЕТРЫ INRANGE
inrange_param_names = ["low_H", "low_S", "low_V", "upp_H", "upp_S", "upp_V"]
low_H = [0, 360]
low_S = [0, 100]
low_V = [0, 100]
upp_H = [360, 360]
upp_S = [100, 100]
upp_V = [100, 100]

# ПАРАМЕТРЫ ADAPTIVETHRESHOLD
adaptiveThreshold_param_names = ["maxValue", "adaptiveMethod", "thresholdType", "blockSize"]
maxValue = [255, 255]
adaptiveMethod = [3, 3]
adaptiveMethods = [
    cv.BORDER_REPLICATE,
    cv.BORDER_ISOLATED,
    cv.ADAPTIVE_THRESH_MEAN_C,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C
]
thresholdType = [0, 1]
thresholdTypes = [
    cv.THRESH_BINARY,
    cv.THRESH_BINARY_INV
]
blockSize = [4, 10]


# ПАРАМЕТРЫ BILATERALFILTER
bilateralFilter_param_names = ["d", "sigmaColor", "sigmaSpace",]
d = [5, 25]
sigmaColor = [20, 50]
sigmaSpace = [20, 50]



if __name__ == "__main__":
    images = [[] for i in range(M)]  # чистые фотографии
    proc_img = [[] for i in range(M)]  # фотографии для обработки
    # открытие изображение
    for i in range(M):
        for j in range(P):
            img = cv.imread(f"./photo/{i + 1}_{j + 1}.jpg")
            images[i].append(img)
            proc = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # изменение цветовой схемы
            # proc = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # изменение цветовой схемы
            proc_img[i].append(proc)
    cv.namedWindow(trackbar_window_name)  # создание окна настроек
    # создание окон для отображения результатов
    for window_name in window_names:
        cv.namedWindow(window_name)


    ####################################################################################################################
    def update():  # функция обновления изображений в окнах в результате изменения параметров
        print("Update!")
        for i in range(len(proc_img)):
            tmp = []
            for j in range(len(proc_img[i])):
                curr = proc_img[i][j].copy()
                # bilateralFilter---------------------------------------------------------------------------------------
                # curr = cv.bilateralFilter(curr, d[0], sigmaColor[0], sigmaSpace[0])
                # adaptiveThreshold-------------------------------------------------------------------------------------
                # curr = cv.adaptiveThreshold(curr, maxValue[0], adaptiveMethods[adaptiveMethod[0]], thresholdTypes[thresholdType[0]], (blockSize[0]+1)*2+1, 2)
                # inRange-----------------------------------------------------------------------------------------------
                # curr = cv.inRange(curr, (low_H[0], low_S[0], low_V[0]), (upp_H[0], upp_S[0], upp_V[0]))
                # Canny-------------------------------------------------------------------------------------------------
                curr = cv.Canny(curr, threshold1[0], threshold2[0], apertureSize[0] + 3)
                # ------------------------------------------------------------------------------------------------------
                contours, hierarchy = cv.findContours(curr, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_KCOS)  # находим контуры
                # отсечение контуров малой площади----------------------------------------------------------------------
                areas = [cv.contourArea(contour) for contour in contours]  # вычисление площади каждого контура
                max_area = max(areas)
                tmp_img = images[i][j].copy()  # копируем изображение
                # for k in range(len(contours)):
                #     if(areas[k] / max_area >= 0.5):
                #         cv.drawContours(tmp_img, contours, k, CONTOUR_COLOR, int(THICKNESS / kx[i]), cv.LINE_AA, hierarchy, 1)
                for k in range(5):
                    print(k)
                    cv.drawContours(tmp_img, contours, areas.index(max(areas)), CONTOUR_COLOR, int(THICKNESS / kx[i]), cv.LINE_AA, hierarchy, 1)
                    areas[areas.index(max(areas))] = 0
                #-------------------------------------------------------------------------------------------------------
                # tmp_img = images[i][j].copy()  # копируем изображение
                # на копии рисуем контуры
                # cv.drawContours(tmp_img, contours, -1, CONTOUR_COLOR, int(THICKNESS / kx[i]), cv.LINE_AA, hierarchy, 1)
                # изменяем размер, чтобы влезло в окно
                tmp_img = cv.resize(tmp_img, None, fx=kx[i], fy=kx[i])
                tmp.append(tmp_img)  # добавление во временный буфер
            horizontal = np.hstack(tmp)  # объединение фотографий
            cv.imshow(window_names[i], horizontal)  # отображение в окне


    # Canny ------------------------------------------------------------------------------------------------------------
    def on_threshold1_trackbar(val):
        global threshold1
        threshold1[0] = val
        update()

    def on_threshold2_trackbar(val):
        global threshold2
        threshold2[0] = val
        update()

    def on_apertureSize_trackbar(val):
        global apertureSize
        apertureSize[0] = val
        update()

    for name in canny_param_names:
        cv.createTrackbar(name, trackbar_window_name, globals()[name][0], globals()[name][1], globals()[f"on_{name}_trackbar"])

    # inRange ----------------------------------------------------------------------------------------------------------
    # def on_low_H_trackbar(val):
    #     global low_H
    #     low_H[0] = val
    #     update()
    #
    # def on_low_S_trackbar(val):
    #     global low_S
    #     low_S[0] = val
    #     update()
    #
    # def on_low_V_trackbar(val):
    #     global low_V
    #     low_V[0] = val
    #     update()
    #
    # def on_upp_H_trackbar(val):
    #     global upp_H
    #     upp_H[0] = val
    #     update()
    #
    # def on_upp_S_trackbar(val):
    #     global upp_S
    #     upp_S[0] = val
    #     update()
    #
    # def on_upp_V_trackbar(val):
    #     global upp_V
    #     upp_V[0] = val
    #     update()
    #
    # for name in inrange_param_names:
    #     cv.createTrackbar(name, trackbar_window_name, globals()[name][0], globals()[name][1], globals()[f"on_{name}_trackbar"])

    # adaptiveThreshold ------------------------------------------------------------------------------------------------
    # def on_maxValue_trackbar(val):
    #     global maxValue
    #     maxValue[0] = val
    #     update()
    #
    # def on_adaptiveMethod_trackbar(val):
    #     global adaptiveMethod
    #     adaptiveMethod[0] = val
    #     update()
    #
    # def on_thresholdType_trackbar(val):
    #     global thresholdType
    #     thresholdType[0] = val
    #     update()
    #
    # def on_blockSize_trackbar(val):
    #     global blockSize
    #     blockSize[0] = val
    #     update()
    #
    # for name in adaptiveThreshold_param_names:
    #     cv.createTrackbar(name, trackbar_window_name, globals()[name][0], globals()[name][1], globals()[f"on_{name}_trackbar"])

    # bilateralFilter --------------------------------------------------------------------------------------------------
    # def on_d_trackbar(val):
    #     global d
    #     d[0] = val
    #     update()
    #
    # def on_sigmaColor_trackbar(val):
    #     global sigmaColor
    #     sigmaColor[0] = val
    #     update()
    #
    # def on_sigmaSpace_trackbar(val):
    #     global sigmaSpace
    #     sigmaSpace[0] = val
    #     update()
    #
    # for name in bilateralFilter_param_names:
    #     cv.createTrackbar(name, trackbar_window_name, globals()[name][0], globals()[name][1], globals()[f"on_{name}_trackbar"])


    update()  # отрисовка изображений

    # ожидание закрытия окон
    cv.waitKey()
    cv.destroyAllWindows()