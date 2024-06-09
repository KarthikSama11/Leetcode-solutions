class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      ans = 0
      umap = {0:1}
      total = 0
      for num in nums:
        total += num
        x = (total)%k
        if x < 0: 
          x += k
        if x not in umap:
          umap[x] = 0 
        ans += umap[x]
        umap[x] += 1
      return ans

