import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<Integer> active = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();
        helper(0, target, candidates, active, ans);
        return ans;
    }

    static void helper(int index, int target, int[] candidates, List<Integer> active, List<List<Integer>> ans) {
        // Base case: if the target is exactly 0, we've found a valid combination
        if (target == 0) {
            ans.add(new ArrayList<>(active));
            return;
        }

        // If the target is negative, we stop exploring this path
        if (target < 0 || index == candidates.length) {
            return;
        }

        // Include the current candidate
        active.add(candidates[index]);
        helper(index, target - candidates[index], candidates, active, ans); // Not moving to the next index
        active.remove(active.size() - 1); // Backtrack

        // Exclude the current candidate and move to the next index
        helper(index + 1, target, candidates, active, ans);
    }
}
