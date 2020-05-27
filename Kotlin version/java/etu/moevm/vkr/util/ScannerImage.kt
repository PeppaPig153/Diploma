package etu.moevm.vkr.util

import android.text.Editable
import android.util.Log
import etu.moevm.vkr.model.StructScanner
import org.opencv.core.*
import org.opencv.imgcodecs.Imgcodecs
import org.opencv.imgproc.Imgproc
import kotlin.collections.ArrayList

class ScannerImage {
    fun findSquare(contours: List<MatOfPoint>, max_1: Int, max_2: Int): DoubleArray {
        // вычисление площади контура
        val contour_area_1 = Imgproc.contourArea(contours[max_1])
        val contour_area_2 = Imgproc.contourArea(contours[max_2])

        // вычисление площадь квадрата
        val contour_ = MatOfPoint2f()
        contours[max_1].convertTo(contour_, CvType.CV_32FC2)
        val rect_1 = Imgproc.minAreaRect(contour_)
        val square_area_1 = rect_1.size.width * rect_1.size.height
        contours[max_2].convertTo(contour_, CvType.CV_32FC2)
        val rect_2 = Imgproc.minAreaRect(contour_)
        val square_area_2 = rect_2.size.width * rect_2.size.height

        // разница площадей и сторон
        val square_diff_1 = Math.abs(contour_area_1 - square_area_1)
        val square_diff_2 = Math.abs(contour_area_2 - square_area_2)
        val side_diff_1 = Math.abs(rect_1.size.width - rect_1.size.height)
        val side_diff_2 = Math.abs(rect_2.size.width - rect_2.size.height)
        val result: DoubleArray

        // оба квадраты
        result =
            if (square_diff_1 < 10 && square_diff_2 < 10 && side_diff_1 < 10 && side_diff_2 < 10) {
                // берём с большей стороной
                if (square_area_1 > square_area_2) {
                    doubleArrayOf(max_1.toDouble(), (rect_1.size.width + rect_1.size.height) / 2)
                } else {
                    doubleArrayOf(max_2.toDouble(), (rect_2.size.width + rect_2.size.height) / 2)
                }
            } else {
                if (side_diff_1 < side_diff_2) {
                    doubleArrayOf(max_1.toDouble(), (rect_1.size.width + rect_1.size.height) / 2)
                } else {
                    doubleArrayOf(max_2.toDouble(), (rect_2.size.width + rect_2.size.height) / 2)
                }
            }
        return result
    }

    fun scan(struct: StructScanner): StructScanner {
        //System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        val filename = struct.pathToFile //"test.jpg"; // Название файла
        val img = Imgcodecs.imread(filename) // чтение из файла
        val k = 300.0 / img.width()
        Imgproc.resize(img, img, Size(), k, k)
        val gray = Mat(img.rows(), img.cols(), img.type())
        // -----------------------------------------------------------------------------------------
//        Imgproc.cvtColor(img, gray, Imgproc.COLOR_RGB2GRAY); // изменение цветовой схемы
//        Mat canny = new Mat(gray.rows(), gray.cols(), gray.type());
//        Imgproc.Canny(gray, canny, 100, 200, 3, false); // Детектор границ Канни
        // -----------------------------------------------------------------------------------------
        Imgproc.cvtColor(img, gray, Imgproc.COLOR_RGB2HSV)
        val thresh = Mat(gray.rows(), gray.cols(), gray.type())
        Core.inRange(gray, Scalar(0.0, 0.0, 80.0), Scalar(180.0, 255.0, 255.0), thresh)
        // -----------------------------------------------------------------------------------------
        // поиск контуров
        val contours: List<MatOfPoint> = ArrayList()
        val hierarchy = Mat()
        Imgproc.findContours(thresh, contours, hierarchy, Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE)
        var max_1 = -1
        var max_2 = -1
        var max_area_1 = -1.0
        var max_area_2 = -1.0
        for (i in contours.indices) {
            val contourArea = Imgproc.contourArea(contours[i])
            if (max_area_2 < contourArea) {
                if (max_area_1 < contourArea) {
                    max_area_2 = max_area_1
                    max_2 = max_1
                    max_area_1 = contourArea
                    max_1 = i
                } else {
                    max_area_2 = contourArea
                    max_2 = i
                }
            }
        }

        // поиск установочного квадрата
        val square_params = findSquare(contours, max_1, max_2)
        var max_index = 0
        max_index = if (max_1 == square_params[0].toInt()) {
            max_2
        } else {
            max_1
        }

        // отрисовка большого контура
        Imgproc.drawContours(img, contours, max_index, Scalar(0.0, 255.0, 0.0), 10)

        // отрисовка квадрата
        Imgproc.drawContours(img, contours, square_params[0].toInt(), Scalar(255.0, 0.0, 0.0), 10)

        // сохранение
        Imgcodecs.imwrite(filename, img)

        // конвертация точек контура в массив double
        val converted_contours: ArrayList<DoubleArray>? = arrayListOf()
        var min_x = contours[max_index].toArray()[0].x
        var min_y = contours[max_index].toArray()[0].y
        for (j in 0 until contours[max_index].rows()) {
            val tmp_point = contours[max_index].toArray()[j]
            converted_contours?.add(doubleArrayOf(tmp_point.x, tmp_point.y))
            if(tmp_point.x < min_x){
                min_x = tmp_point.x
            }
            if(tmp_point.y < min_y){
                min_y = tmp_point.y
            }
        }
        // перевод каждого контура в угол (0,0)
        if (converted_contours != null) {
            for (j in 0 until converted_contours.size) {
                converted_contours[j][0] -= min_x
                converted_contours[j][1] -= min_y
            }
        }
        struct.arrPoint = converted_contours
        struct.square = square_params[1]
        return struct
    }

    fun resizeContours(contours_list: List<StructScanner>, square_size: Double, width: Double, length: Double): ArrayList<Double> {
        // минимальное значения длины стороны квадрата
        var new_square = contours_list[0].square!!
        for (i in 0 until contours_list.size) {
            if(new_square > contours_list[i].square!!) {
                    new_square = contours_list[i].square!!
                }
        }

        // новые значение для прямоугольника
        val new_width = width * new_square / square_size
        val new_length = length * new_square / square_size
        var max_x = 0.0
        var max_y = 0.0
        var number_of_figures = 0.0

        // скалирование контуров
        for (i in 0 until contours_list.size) { // по контурам
            number_of_figures += contours_list[i].counter
            val k = new_square / contours_list[i].square!!;
            for (j in 0 until (contours_list[i].arrPoint?.size ?: 0)){ // по точкам
                // масштабированные значения точек
                contours_list[i].arrPoint?.get(j)?.set(0, (contours_list[i].arrPoint?.get(j)?.get(0) ?: 0.0)*k)
                contours_list[i].arrPoint?.get(j)?.set(1, (contours_list[i].arrPoint?.get(j)?.get(1) ?: 0.0)*k)
                // проверка на максимальное значение высоты и ширины
                val point = contours_list[i].arrPoint?.get(j)
                if(point?.get(0)!! > contours_list[i].length!!){
                    contours_list[i].length = point.get(0)
                }
                if(point.get(0) > max_x){
                    max_x = point.get(0)
                }
                if(point.get(1) > max_y){
                    max_y = point.get(1)
                }
            }
        }

        return arrayListOf(new_width, new_length, max_x, max_y, number_of_figures)
    }
}