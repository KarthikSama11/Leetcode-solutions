class Solution {
    public long findMaximumScore(List<Integer> nums) {
        long res = 0;  // Changed to long to match the return type
        int l = 0;     // Left boundary for the segment
        for (int i = 1; i < nums.size(); i++) {
            if (nums.get(i) > nums.get(l) || i == nums.size() - 1) {
                res += (i - l) * (long)nums.get(l); // Ensure nums.get(l) is cast to long for multiplication
                l = i;  // Update left boundary
            }
        }
        return res;
    }
}
