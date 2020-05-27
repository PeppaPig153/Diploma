package etu.moevm.vkr.util

import android.util.Log
import etu.moevm.vkr.model.StructScanner
import etu.moevm.vkr.ui.Activity.MainActivity
import java.io.FileWriter
import java.io.IOException
import java.lang.Double.max

object SVGwriter {
    fun write(contours_list: List<StructScanner>, width: Double, length: Double, max_x: Double, max_y: Double, counter: Int, filename: String, path: String?):String {
        // размеры файла
        var main_width = max(2*length, max_x) + 10
        var main_height = 0.0


        val polygon_template_start =
            "<polygon fill=\"none\" stroke=\"#010101\" stroke-miterlimit=\"10\" points=\""
        val polygon_template_end = "\"/>"
        var polygons =
            "<rect width=\"$length\" height=\"$width\" fill=\"none\" stroke=\"#010101\" class=\"bin\" transform=\"translate(0 0)\"/>"


        // текущие координаты верхнего левого места
        var curr_0_y = width + 10 // строка
        var curr_0_x = 0.0 // столбец

        // цикл записи полигонов в polygons
        for (i in 0 until contours_list.size) { // по контурам
            for (j in 0 until contours_list[i].counter) { // по количеству контура
                // проверка, что выход за правую границу
                if(curr_0_x + contours_list[i].length!! > main_width){
                    curr_0_x = 0.0
                    curr_0_y += max_y
                }
                // текстовое представление контура
                polygons += polygon_template_start
                for (k in 0 until (contours_list[i].arrPoint?.size ?: 0)) {// по точкам
                    polygons += (contours_list[i].arrPoint?.get(k)?.get(0)?.plus(curr_0_x)).toString() + "," + (contours_list[i].arrPoint?.get(k)?.get(1)
                        ?.plus(curr_0_y)).toString() + " "
                }
                polygons += polygon_template_end
                curr_0_x += contours_list[i].length!! + 1
            }
        }

        main_height = curr_0_y + max_y + 10


        val svg_settings =
            "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" id=\"svg\" x=\"0px\" y=\"0px\" width=\"$main_width\" height=\"$main_height\" viewBox=\"0 0 $main_width $main_height\" enable-background=\"new 0 0 $main_width $main_height\" xml:space=\"preserve\">"

        try {
            FileWriter("$path/$filename.svg", false).use { writer ->
                val text = "$svg_settings$polygons</svg>"
                writer.write(text)
                writer.flush()
            }
        } catch (ex: IOException) {
            println(ex.message)
        }
        return "$path/$filename.svg"
    }
}