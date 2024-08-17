class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
      umap = defaultdict(list)
      ans = 0
      for i in range(0,len(nums)):
        num = nums[i]
        if k - num in umap and len(umap[k-num]) > 0:
          ans += 1
          umap[k - num].pop()
          continue
        umap[num].append(i)

      return ans   