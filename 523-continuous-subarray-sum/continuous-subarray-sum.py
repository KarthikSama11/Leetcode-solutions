class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
      if len(nums) <= 1:
        return False
      lookup = {0 : -1}
      prefix = 0
      for i in range(len(nums)):
        prefix += nums[i]
        prefix %= k
        if prefix in lookup :
          if i - lookup[prefix] > 1:
            return True 
        else:
          lookup[prefix] = i
      return False


      


        