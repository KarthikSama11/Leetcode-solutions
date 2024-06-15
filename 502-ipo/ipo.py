class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap = []
        minheap = []
        for i in range(len(profits)):
          heappush(minheap, (capital[i],profits[i]))
        while k:
          while minheap and minheap[0][0] <= w:
            c,p = heappop(minheap)
            heappush(maxheap,-p)
          if not maxheap: break
          w -= heappop(maxheap)
          k -= 1
        return w