class Solution {
    public int maxProfit(int[] prices) {
        // Check if prices array is empty
        if (prices.length == 0) {
            return 0;
        }

        int maxProfit = 0;
        int minValue = prices[0]; // Initialize to the first price

        for (int i = 1; i < prices.length; i++) {
            if (minValue > prices[i]) {
                minValue = prices[i]; // Update the minimum price
            }

            // Calculate potential profit
            int potentialProfit = prices[i] - minValue;
            if (maxProfit < potentialProfit) {
                maxProfit = potentialProfit; // Update max profit if current is higher
            }
        }
        return maxProfit;
    }
}
