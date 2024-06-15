class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
      minheap = []
      for i in range(len(nums)):
        heappush(minheap,nums[i])
      while k:
        x = heappop(minheap) + 1
        heappush(minheap,x) 
        k -= 1
      if minheap and minheap[0] ==0 :
        return 0
      print(minheap)
      ans = 1
      mod = 1e9 + 7
      while minheap:
        ans = ans * heappop(minheap)
        ans %= mod
      return int(ans%mod)
