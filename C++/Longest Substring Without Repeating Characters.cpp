#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> m; // Map to store the frequency of characters
        int maxLength = 0; // To keep track of the maximum length
        int i = 0; // Left pointer

        for (int j = 0; j < s.size(); j++) { // Right pointer
            m[s[j]]++; // Increment frequency of the current character
            
            // If the current character's frequency is more than 1, we have a duplicate
            while (m[s[j]] > 1) {
                m[s[i]]--; // Decrease frequency of the left character
                i++; // Move the left pointer to the right
            }
            
            // Update the maximum length found so far
            maxLength = max(maxLength, j - i + 1);
        }

        return maxLength; // Return the length of the longest substring without repeating characters
    }
};
