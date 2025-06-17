class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for e, p in zip(edges, succProb):
            u,v = e
            adj[u].append((v, p))
            adj[v].append((u, p))
        maxprob = {}
        maxheap = [(-1, start_node)]
        heapify(maxheap)
        print(type(maxheap))
        while maxheap:
            p1, n1 = heappop(maxheap)
            print(p1,n1)
            p1 *= -1
            if n1 == end_node:
                return p1
            if n1 in maxprob:
                continue
            maxprob[n1] = p1
            for n2, p2 in adj[n1]:
                heappush(maxheap,((-1*p2*p1), n2))
        return 0

