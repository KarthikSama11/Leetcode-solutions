class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      umap = {}
      for i in range(len(nums)):
        if target - nums[i] in umap: 
          return [i,umap[target-nums[i]]]
        umap[nums[i]] = i