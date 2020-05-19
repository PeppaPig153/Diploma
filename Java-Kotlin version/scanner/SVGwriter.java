package com.company;
import java.io.*;
import java.util.List;

public class SVGwriter {

    public static void SVGwriter(List<double[]> contours, int[] counters){
        String svg_settings = "<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" version=\"1.1\" id=\"svg2\" x=\"0px\" y=\"0px\" width=\"1147.592px\" height=\"1397.27px\" viewBox=\"0 0 1147.592 1397.27\" enable-background=\"new 0 0 1147.592 1397.27\" xml:space=\"preserve\">";
        String polygon_template_start = "<polygon fill=\"none\" stroke=\"#010101\" stroke-miterlimit=\"10\" points=\"";
        String polygon_template_end = "\"/>";
        String polygons = "";

        // цикл записи полигонов в polygons
        for(int i=0; i<contours.size(); i++){
            polygons += polygon_template_start;
            for(int j=0; j<contours.get(i).length; j+=2){
                polygons += contours.get(i)[j] + "," + contours.get(i)[j+1] + " ";
            }
            polygons += polygon_template_end;
        }

        try(FileWriter writer = new FileWriter("prob.svg", false)) {
            String text = svg_settings + polygons + "</svg>";
            writer.write(text);
            writer.flush();
        }
        catch(IOException ex){
            System.out.println(ex.getMessage());
        }
    }

    public static void main(String[] args) {
        System.out.println("Привет!");
//        SVGwriter();
    }
}
