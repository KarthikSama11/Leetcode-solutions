class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        vis = set()
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(i):
            if i in vis:
                return
            vis.add(i)
            for node in adj[i]:
                dfs(node)
            return 
        for i in range(n):
            if i not in vis:
                ans += 1
                dfs(i)
        return ans