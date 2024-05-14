class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      maxheap = []
      for stone in stones:
        heappush(maxheap, -stone)
      while len(maxheap) > 1:
        one = heappop(maxheap)
        two = heappop(maxheap)
        val = abs(one - two)
        if val:
          heappush(maxheap,-val)
      if len(maxheap): return -heappop(maxheap)
      return 0