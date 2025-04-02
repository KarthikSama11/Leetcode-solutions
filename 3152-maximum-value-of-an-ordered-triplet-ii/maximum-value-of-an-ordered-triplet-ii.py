class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        prefixes = [0]*N
        suffixes = [0]*N
        leftmax = 0
        rightmax = 0
        ans = 0
        for i in range(N - 1):
            prefixes[i] = leftmax
            leftmax = max(leftmax, nums[i])
        for k in range(N - 1, 0, -1):
            suffixes[k] = rightmax
            rightmax = max(rightmax, nums[k])
        # print(nums)
        # print(prefixes)
        # print(suffixes)
        for j in range(1, N - 1):
            ans = max(ans, (prefixes[j] - nums[j])*suffixes[j])
        return ans
