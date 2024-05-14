class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
      pq = []
      hashmap = {}
      time = 0
      for t in tasks:
        if t in hashmap and hashmap[t] >= time:
          time = hashmap[t]
        hashmap[t] = time + space + 1
        time += 1
      return time

          