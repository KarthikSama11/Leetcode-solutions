class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
      ans = 0
      maxsofar = 0
      for i, num in enumerate(nums):
        ans += maxsofar
        maxsofar = max(maxsofar, num)
      return ans