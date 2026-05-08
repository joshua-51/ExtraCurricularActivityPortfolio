package JavaMethodsPractice;
import java.util.Scanner;

public class methods {
    private static void hello(String name) {
        System.out.println("hello "+ name);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("What is your name? ");
        String name = scanner.nextLine();
        hello(name);
        scanner.close();
    }
}
