package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.opencv.core.*;
import org.opencv.imgproc.Imgproc;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Moments;


public class Main {
    public static int isRectangle(double square_difference, double side_difference){
        // на какую величину могут допустимо отличаться
        double square_delta = 10.0; // площади
        double side_delta = 10.0; // стороны
        if(square_difference <= square_delta && side_difference <= side_delta){
            return 0;
        }
        if(square_difference <= square_delta && side_difference > side_delta){
            return 1;
        }
        if(square_difference > square_delta && side_difference <= side_delta){
            return 2;
        }
        if(square_difference > square_delta && side_difference > side_delta){
            return 3;
        }
        return 4;
    }

    public static double[] findSquare(List<MatOfPoint> contours){
        // сведения о наиболее подходящей на роль квадрата контура
        int index = 0;
        double square_difference = 0.0;
        double side_difference = 0.0;
        double avg_side_length = 0.0;

        // проверка контуров
        for (int i = 0; i < contours.size(); i++){
            // вычисление площади контура
            double contour_area = Imgproc.contourArea(contours.get(i));
            // вычисление площадь квадрата
            MatOfPoint2f contour_ = new MatOfPoint2f();
            contours.get(i).convertTo(contour_, CvType.CV_32FC2);
            RotatedRect rect = Imgproc.minAreaRect(contour_);
            double square_area = rect.size.width*rect.size.height;
            // разница площадей и сторон
            double square_diff = Math.abs(contour_area - square_area);
            double side_diff = Math.abs(rect.size.width-rect.size.height);

            // уровень соответствия прямоугольнику
            int curr_result = isRectangle(square_difference, side_difference);
            int tmp_result = isRectangle(square_diff, side_diff);

            // если первый или
            // предыдущий кандидат не вписывался в нормы и новый меньше его разниться в площади или
            // предыдущий кандидат вписывается в нормы по разности площади, но не по сторонам - значит он прямоугольник
            // оба квадраты, берём с большей длиной стороны
            if(i==0 || (curr_result > 1 && square_diff < square_difference) ||
                    (curr_result == 1 && (tmp_result == 0 || (tmp_result == 1 && side_diff < side_difference))) ||
                    (curr_result == 0 && tmp_result == 0 && (rect.size.width+rect.size.height)/2 > avg_side_length)){
                    index = i;
                    square_difference = square_diff;
                    side_difference = side_diff;
                    avg_side_length = (rect.size.width+rect.size.height)/2;
            }
        }
        double[] result = {index, avg_side_length};
        return result;
    }

    public static List<double[]> resizeContours (List<MatOfPoint> contours, double[] square_size){
        List<double[]> scaled_contours = new ArrayList<double[]>();
        // среднее значения длины стороны
        double avg_size = Arrays.stream(square_size).sum()/square_size.length;

        // скалирование
        for (int i = 0; i < contours.size(); i++) {
            Moments moments = Imgproc.moments(contours.get(i));
            int cx = (int)(moments.m10/moments.m00);
            int cy = (int)(moments.m01/moments.m00);
            for(int j=0; j<contours.get(i).rows(); j++){
                Point tmp_point = contours.get(i).toArray()[j];
                tmp_point.x = (tmp_point.x - cx) * (avg_size / square_size[i]) + cx;
                tmp_point.y = (tmp_point.y - cy) * (avg_size / square_size[i]) + cy;
                scaled_contours.add(new double[]{tmp_point.x, tmp_point.y});
            }

        }
        return scaled_contours;
    }

    public static void main(String[] args) {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        String filename = "test.jpg"; // Название файла
        Mat img = Imgcodecs.imread(filename); // чтение из файла
        Mat gray = new Mat(img.rows(), img.cols(), img.type());
        Imgproc.cvtColor(img, gray, Imgproc.COLOR_RGB2GRAY); // изменение цветовой схемы
        Mat canny = new Mat(gray.rows(), gray.cols(), gray.type());
        Imgproc.Canny(gray, canny, 100, 200, 3); // Детектор границ Канни
        // поиск контуров
        List<MatOfPoint> contours = new ArrayList<>();
        Mat hierarchy = new Mat();
        Imgproc.findContours(canny, contours, hierarchy, Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_SIMPLE);

        // поиск установочного квадрата
        double[] square_params = findSquare(contours);

        // определение площади оставшихся контуров и нахождение самого большого
        double max_area = 0.0;
        int max_index = 0;
        for (int i = 0; i < contours.size(); i++) {
            System.out.println(contours.get(i).getClass());
            double contourArea = Imgproc.contourArea(contours.get(i));
            if (max_area < contourArea && i != (int) square_params[0]) {
                max_area = contourArea;
                max_index = i;
            }
        }

        // отрисовка большого контура
        Imgproc.drawContours(img, contours, max_index, new Scalar(0,255,0), 10);
        // отрисовка квадрата
        Imgproc.drawContours(img, contours, (int) square_params[0], new Scalar(255,0,0), 10);
        Imgcodecs.imwrite("new_photo.jpg", img);


        // Преобразование в массив точек
        Point[] contour_points = contours.get(4).toArray();
        System.out.println(Arrays.toString(contour_points));
        System.out.println(contour_points[0].x);
    }

}
