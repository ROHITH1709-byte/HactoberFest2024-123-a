import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] arr, int target) {
        int len = arr.length;
        int[] res = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>(); // Specify the types
        
        for (int i = 0; i < len; i++) {
            int complement = target - arr[i];
            if (map.containsKey(complement)) {
                res[0] = map.get(complement); // Use the stored index
                res[1] = i;
                return res;
            }
            map.put(arr[i], i); // Store index of the current element
        }
        // If no solution is found, you can choose to return null or throw an exception
        return null; // or throw new IllegalArgumentException("No two sum solution");
    }
}
