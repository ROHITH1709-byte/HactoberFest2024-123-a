class Solution {
    public int maxSubArray(int[] nums) {
        int currentMax = 0;
        int max = Integer.MIN_VALUE; // Initialize to the smallest possible integer

        for (int num : nums) {
            currentMax += num; // Add current number to the currentMax

            if (currentMax > max) {
                max = currentMax; // Update max if currentMax is greater
            }

            if (currentMax < 0) {
                currentMax = 0; // Reset currentMax if it becomes negative
            }
        }

        return max; // Return the maximum subarray sum
    }
}
