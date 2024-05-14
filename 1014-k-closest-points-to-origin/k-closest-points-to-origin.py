class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      maxheap = []
      for x,y in points:
        dist = x**2 + y**2
        heappush(maxheap, (-dist,x, y))
        if len(maxheap) > k: heappop(maxheap)
      ans = []
      while len(maxheap):
        _,x,y = heappop(maxheap)
        ans.append([x,y])
      return ans