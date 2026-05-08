package LEARNING.JavaTutorial;
import java.util.Scanner;

public class ifElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = scanner.nextInt();
        if(age >= 18 && age <= 65) {
        System.out.println("You are an adult!");
        }
        else if(age >= 65){
            System.out.println("YOU ARE OLD!");
        }
        else if(age < 0){
            System.out.println("You haven't been born yet!");
        }
        else if(age == 0){
            System.out.println("You are a baby");
        }
        else{
            System.out.println("You are a child!");
        }
        scanner.close();


    }
}