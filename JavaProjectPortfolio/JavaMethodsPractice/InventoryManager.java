package JavaMethodsPractice;
public class InventoryManager {
    public static void main(String[] args) {
        double[] prices = {2.12, 3.99, 43.67, 32.45, 53.23};
        applyDiscount(prices, 0.20);
    } 
    static void applyDiscount(double[]prices, double discount) {
        for (double price:prices) {
            System.out.println("$"+price);
        }
        
        double finalTotal = 0;

        for (int i = 0; i < prices.length; i++){
            double new_price = prices[i] * discount;
            prices[i] = new_price;
            finalTotal += new_price;
        }

        if (finalTotal > 100) {
            finalTotal -= 5;
        }

        System.out.println("Your total is $" + finalTotal + "!");
    }
}