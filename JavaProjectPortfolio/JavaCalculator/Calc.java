package JavaCalculator;

import java.util.Scanner;
public class Calc {

    static float addition(float x, float y) {
        float z = x+y;
        return z;
    }

    static float subtraction(float x, float y) {
        float z = x-y;
        return z;
    }

    static float multiplication(float x, float y) {
        float z = x*y;
        return z;
    }

    static float division(float x, float y) {
        float z = x/y;
        return z;
    }

    static String userInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Do you want to add, subtract, divide or multiply? ");
        String decision = scanner.nextLine();
        scanner.close();
        return decision;
    }

    static double xyquestion(String operator) {
        Scanner scanner = new Scanner(System.in);
        if (operator == "add"){
            System.out.print("What is x in x + y: ");
            float x = scanner.nextFloat();
            System.out.print("What is y in x + y: ");
            float y = scanner.nextFloat();
            scanner.close();
            return addition(x, y);
        } else if (operator == "subtract") {
            System.out.print("What is x in x - y: ");
            float x = scanner.nextFloat();
            System.out.print("What is y in x - y: ");
            float y = scanner.nextFloat();
            scanner.close();
            return subtraction(x, y);
        } else if (operator == "divide"){
            System.out.print("What is x in x ÷ y: ");
            float x = scanner.nextFloat();
            System.out.print("What is y in x ÷ y: ");
            float y = scanner.nextFloat();
            scanner.close();
            return division(x, y);
        } else if (operator == "multiply"){
            System.out.print("What is x in x * y: ");
            float x = scanner.nextFloat();
            System.out.print("What is y in x * y: ");
            float y = scanner.nextFloat();
            scanner.close();
            return multiplication(x, y);
        } else {
            scanner.close();
            return 1;
        }
    }

    static void main() {
        int x = 0;
        while (x != 1) {
            String operater = userInput();
            double ans = xyquestion(operater);
            if (ans == 1) {
                x = (int) ans;
            }
        }
    }
    public static void main(String[] args) {
        main();
    }
}