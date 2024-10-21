class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = set()
        adj = defaultdict(list)
        ans = True
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        def dfs(i):
            if i in vis:
                return
            vis.add(i)
            for node in adj[i]:
                dfs(node)
            return
        dfs(0)
        if len(vis) != n:
            return False
        if len(edges) + 1 != n:
            return False
        return True
