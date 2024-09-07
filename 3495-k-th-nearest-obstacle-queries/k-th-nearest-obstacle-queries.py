class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
      maxheap = []
      ans = []
      for x,y in queries:
        heappush(maxheap, -(abs(x) + abs(y)))
        if len(maxheap) > k:
          heappop(maxheap)

        if len(maxheap) < k:
          ans.append(-1)
        else:
          ans.append(-maxheap[0])
      return ans    