package LEARNING.JavaImportClasses;
import java.util.Scanner;

public class userInput {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
 
        System.out.println("Enter your age");
        int age = scanner.nextInt();

        System.out.println("What is your GPA? ");
        double gpa = scanner.nextDouble();
        
        System.out.println("Are you a student? (true/false) ");
        boolean isStudent = scanner.nextBoolean();

        System.out.println("Hello " + name);
        System.out.println("You are " + age + " years old");
        System.out.println("Your GPA is " + gpa);
        System.out.println("Student: " + isStudent);

        scanner.close();
    }
}