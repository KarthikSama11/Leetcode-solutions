class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(set)
        if n == 1 and not len(trust):
            return 1
        for u, v in trust:
            adj[v].add(u)
        res = -1
        print(adj)
        for person in adj:
            if len(adj[person]) == n - 1:
                flag = True
                for node in adj:
                    if person in adj[node]:
                        flag = False
                if flag:
                    return person
        return -1

        
