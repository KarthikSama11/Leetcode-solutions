import functools
class Solution:
    
    def frequencySort(self, nums: List[int]) -> List[int]:
      freq = collections.Counter(nums)
      print(freq)
      
      ans = sorted(nums, key = lambda x: (freq[x], -x))
      return ans