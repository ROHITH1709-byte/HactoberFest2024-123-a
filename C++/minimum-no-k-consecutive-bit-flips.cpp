#include <vector>
using namespace std;

class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int n = nums.size();
        int flips = 0; // Count of total flips
        int flipEffect = 0; // Tracks the current effect of flips

        for (int i = 0; i < n; ++i) {
            // If the flipEffect is odd, the current element is flipped
            if (flipEffect % 2 != 0) {
                nums[i] = 1 - nums[i];
            }

            // If the current element is 0 after considering flips, we need to flip
            if (nums[i] == 0) {
                if (i + k > n) {
                    return -1; // Not enough elements left to flip
                }
                flips++; // Increment flip count
                flipEffect++; // Start a new flip effect
                if (i + k < n) {
                    // To counteract the flip effect after k elements
                    flipEffect--; // We will negate this flip effect after k elements
                }
            }
        }

        return flips; // Return the total number of flips
    }
};
