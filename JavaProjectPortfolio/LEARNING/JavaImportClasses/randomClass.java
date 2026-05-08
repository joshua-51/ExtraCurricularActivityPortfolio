package LEARNING.JavaImportClasses;
import java.util.Random;

public class randomClass {
    public static void main(String[] args) {

        Random random = new Random();
        
        int num1;
        double num2;
        boolean isHeads;

        num1 = random.nextInt( 1,7); // numbers from 1 - 6, the origin is inclusive, the bound is exclusive
        num2 = random.nextDouble(); // numbers between 0 and 1
        isHeads = random.nextBoolean(); // return either true or false
        
        System.out.println(num1);
        System.out.println(num2);
        System.out.println(isHeads);
        
    }
}
