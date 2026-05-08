package JavaCalculator;
import java.util.Scanner;
public class compoundInterestCalculator {

    public double principal;
    public double rate;
    public int timesCompound;
    public int years;
    public double amount;

    static double amount(double principal, double rate, int timesCompounded, int years) {
        return principal * Math.pow(1+rate / timesCompounded, timesCompounded * years);
    }
    public static void main(String[] args) {

        compoundInterestCalculator arguments = new compoundInterestCalculator();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the principal amount: ");
        arguments.principal = scanner.nextDouble();
        System.out.print("Enter the interest rate (in %): ");
        arguments.rate = scanner.nextDouble() / 100;
        System.out.print("Enter the # of times compounded yearly: ");
        arguments.timesCompound = scanner.nextInt();
        System.out.print("Enter the number of years: ");
        arguments.years = scanner.nextInt();

        scanner.close();

        System.out.println("The amount after "+ arguments.years+" years is $"+amount(arguments.principal, arguments.amount, arguments.timesCompound, arguments.years));
    }
}
