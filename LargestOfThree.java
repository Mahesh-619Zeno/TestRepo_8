import java.util.Scanner;

public class LargestOfThree {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double firstNumber = getValidNumber(scanner);

        System.out.print("Enter second number: ");
        double num2 = getValidNumber(scanner);

        System.out.print("Enter third number: ");
        double num3 = getValidNumber(scanner);

        double largest = Math.max(Math.max(num1, num2), num3);

        System.out.printf("The largest number is: %.2f%n", largest);

        scanner.close();
    }

    private static double getValidNumber(Scanner scanner) {
        while (!scanner.hasNextDouble()) {
            System.out.println("Invalid input. Please enter a valid number.");
            scanner.next(); // Clear the invalid input
        }
        return scanner.nextDouble();
    }
}
