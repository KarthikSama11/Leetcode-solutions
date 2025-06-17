class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = -1
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])

        minheap = [(0, k)]
        heapify(minheap)
        shortest = {}
        while minheap:
            c1, n1 = heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = c1
            res = max(res, c1)
            for n2, c2 in adj[n1]:
                heappush(minheap, (c2 + c1, n2))
        return -1 if res == 0 or len(shortest) < n  else res
            

        