from typing import List

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        # Initialize the result variable 'ans' to store the final sum of power
        # 't' is a temporary variable to accumulate the sum of powers
        # 'base' is used to perform modulo 10^9 + 7 to prevent integer overflow
        ans, t, base = 0, 0, 10**9 + 7
        
        # Iterate over the sorted 'nums' list
        for c in sorted(nums):
            # Update 'ans' by adding the current power contribution for this element 'c'
            # Formula: (previous_sum + current_element) * current_element^2
            ans = (ans + (t + c) * c * c) % base
            
            # Update 't' for the next iteration
            t = (2 * t + c) % base
        
        # Return the final sum of powers modulo 10^9 + 7
        return ans

# Example usage
solution = Solution()
nums = [1, 2, 3]
result = solution.sumOfPower(nums)
print("The sum of power is:", result)
