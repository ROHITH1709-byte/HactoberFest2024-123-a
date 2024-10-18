public class PowerUsingLoop {
    public static void main(String[] args) {
        int base = 2;
        int exponent = 3; // You can change this to test negative values
        double result = 1; // Use double to handle fractional results for negative exponents

        // Handle negative exponents
        if (exponent < 0) {
            for (int i = 1; i <= -exponent; i++) {
                result *= 1.0 / base; // Use reciprocal for negative exponent
            }
        } else {
            for (int i = 1; i <= exponent; i++) {
                result *= base;
            }
        }

        System.out.println("Result: " + result);
    }
}
