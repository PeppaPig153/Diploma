package com.company;

import java.util.ArrayList;
import java.util.List;

import org.opencv.core.*;
import org.opencv.imgproc.Imgproc;
import org.opencv.imgcodecs.Imgcodecs;


public class Main {
    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        String filename = "./photo/3_3.jpg"; // Название файла
        Mat img = Imgcodecs.imread(filename); // чтение из файла
        Mat gray = new Mat(img.rows(), img.cols(), img.type());
        Imgproc.cvtColor(img, gray, Imgproc.COLOR_RGB2GRAY); // изменение цветовой схемы
        Mat canny = new Mat(gray.rows(), gray.cols(), gray.type());
        Imgproc.Canny(gray, canny, 100, 200, 3); // Детектор границ Канни
        // поиск контуров
        List<MatOfPoint> contours = new ArrayList<>();
        Mat hierarchy = new Mat();
        Imgproc.findContours(canny, contours, hierarchy, Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE);
        // определение площади контуров и нахождение самого большого
        double max_area = 0.0;
        int max_index = 0;
        for (int i = 0; i < contours.size(); i++) {
            double contourArea = Imgproc.contourArea(contours.get(i));
            if (max_area < contourArea) {
                max_area = contourArea;
                max_index = i;
            }
        }
        // отрисовка только больших контуров
        Imgproc.drawContours(img, contours, max_index, new Scalar(0,255,0), 10);

        Imgcodecs.imwrite("new_photo.jpg", img);

        System.out.println(contours.size());
    }

}
