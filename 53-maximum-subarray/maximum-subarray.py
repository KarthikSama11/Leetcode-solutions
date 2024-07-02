class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      ans = nums[0]
      total = nums[0]
      for i in range(1, len(nums)):
        if total < 0:
          total = 0
        total += nums[i]
        ans = max(ans, total)
      return ans