class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
      pq = []
      queue = deque()
      mapp = {}
      for t in tasks:
        if t not in mapp: mapp[t] = 0
        mapp[t] += 1
      for k,v in mapp.items():
        heappush(pq,-v)
      print(pq)
      time = 0
      while len(pq) or len(queue):
        if len(queue) and queue[0][1] == time:
          heappush(pq,queue[0][0])
          queue.popleft()
        time += 1
        if len(pq):
          cur = heappop(pq)
          cur += 1
          if cur != 0: queue.append((cur, time + n))

      return time