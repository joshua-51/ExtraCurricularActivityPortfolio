package LEARNING.JavaTutorial;

public class javaArrays {
    public static void main(String[] args) {
        
        // Changing a value in an array
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        cars[0] = "Opel";
        System.out.println(cars[0]);

        // Array length
        System.out.println(cars.length);

        /*
        String[] cars = new String[4];

        You can define later
        */

        /*
        MULTIDIMENSIONAL ARRAY:

        int[][] myNums = {{1,4,2},{3,6,8}}
        */
    }
    
}
