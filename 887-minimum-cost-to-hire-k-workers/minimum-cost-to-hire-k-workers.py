class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
      ans = 1e9
      pq = []
      rates = []
      for i in range(len(wage)):
        rates.append((wage[i]/quality[i],quality[i]))
      rates.sort()
      total = 0
      for rate, qual in rates:
        heappush(pq, -qual)
        total += qual
        if len(pq) > k:
          total += heappop(pq)
        if len(pq) == k:
          ans = min(ans, total*rate)
      return ans

      

      
