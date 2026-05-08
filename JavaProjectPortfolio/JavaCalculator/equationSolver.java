package JavaCalculator;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class equationSolver {

    // Nested private static class to represent a single term in an equation
    private static class Term {
        private double coefficient;
        private String variable;

        public Term(double coefficient, String variable) {
            this.coefficient = coefficient;
            this.variable = variable;
        }

        public double getCoefficient() {
            return coefficient;
        }

        public String getVariable() {
            return variable;
        }

        
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("This program simplifies and solves a system of two linear equations.");
        System.out.println("Enter two equations with x, y, constants, and operators (+, -).");
        System.out.println("Example: 2x + 3y - 5 = 10");

        try {
            System.out.print("Enter the first equation: ");
            String eq1 = scanner.nextLine();
            System.out.print("Enter the second equation: ");
            String eq2 = scanner.nextLine();

            double[] eq1Coeffs = parseEquation(eq1);
            double[] eq2Coeffs = parseEquation(eq2);

            System.out.println("\nSimplified Equations:");
            System.out.printf("Equation 1: %.2fx + %.2fy = %.2f\n", eq1Coeffs[0], eq1Coeffs[1], eq1Coeffs[2]);
            System.out.printf("Equation 2: %.2fx + %.2fy = %.2f\n", eq2Coeffs[0], eq2Coeffs[1], eq2Coeffs[2]);

            solveSystem(eq1Coeffs[0], eq1Coeffs[1], eq1Coeffs[2], eq2Coeffs[0], eq2Coeffs[1], eq2Coeffs[2]);

        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
            System.err.println("Please ensure equations are in a valid format, e.g., '2x + 3y = 5'.");
        } finally {
            scanner.close();
        }
    }

    // Parses a string equation and returns coefficients in the form [a, b, c]
    private static double[] parseEquation(String equation) {
        double a = 0, b = 0, c = 0;
        
        // Normalize the equation: remove spaces and handle implicit '1' coefficients
        String normalizedEq = equation.replaceAll("\\s+", "");
        
        String[] parts = normalizedEq.split("=");
        String leftSide = parts[0];
        String rightSide = parts.length > 1 ? parts[1] : "0";

        List<Term> leftTerms = tokenize(leftSide);
        List<Term> rightTerms = tokenize(rightSide);
        
        // Sum terms on both sides, then move terms to the correct side
        for (Term term : leftTerms) {
            if (term.getVariable().equals("x")) a += term.getCoefficient();
            else if (term.getVariable().equals("y")) b += term.getCoefficient();
            else c -= term.getCoefficient();
        }

        for (Term term : rightTerms) {
            if (term.getVariable().equals("x")) a -= term.getCoefficient();
            else if (term.getVariable().equals("y")) b -= term.getCoefficient();
            else c += term.getCoefficient();
        }
        
        return new double[]{a, b, c};
    }

    // Splits an expression string into a list of Terms
    private static List<Term> tokenize(String expression) {
        List<Term> terms = new ArrayList<>();
        // Handle leading operators (e.g., "-x + 5")
        if (expression.startsWith("-") || expression.startsWith("+")) {
            expression = " " + expression; // Add space to separate leading operator
        }

        // Use a regular expression to find all terms
        Pattern pattern = Pattern.compile("([+-]?[\\d.]*?)([xy]?)");
        Matcher matcher = pattern.matcher(expression);
        
        while (matcher.find()) {
            String fullMatch = matcher.group(0);
            if (fullMatch.isEmpty() || fullMatch.matches("\\s*")) continue;
            
            String coeffStr = matcher.group(1);
            String var = matcher.group(2);
            
            double coeff;
            if (var.isEmpty()) { // Constant term
                coeff = Double.parseDouble(fullMatch);
            } else { // Variable term
                if (coeffStr == null || coeffStr.isEmpty()) {
                    coeff = 1.0;
                } else if (coeffStr.equals("-")) {
                    coeff = -1.0;
                } else if (coeffStr.equals("+")) {
                    coeff = 1.0;
                } else {
                    coeff = Double.parseDouble(coeffStr);
                }
            }
            terms.add(new Term(coeff, var));
        }
        return terms;
    }

    // Solves a system of two linear equations using Cramer's Rule
    private static void solveSystem(double a, double b, double c, double d, double e, double f) {
        double determinant = a * e - b * d;

        if (determinant == 0) {
            if (c * e - b * f == 0 && a * f - c * d == 0) {
                System.out.println("\nThe system has infinite solutions.");
            } else {
                System.out.println("\nThe system has no solution.");
            }
        } else {
            double x = (c * e - b * f) / determinant;
            double y = (a * f - c * d) / determinant;
            System.out.println("\nSolution:");
            System.out.printf("x = %.2f\n", x);
            System.out.printf("y = %.2f\n", y);
        }
    }
}
