class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        provinces = 0
        n = len(isConnected)
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    adj[r].append(c)
                    adj[c].append(r)
        def dfs(i):
            if i in vis:
                return
            vis.add(i)
            for node in adj[i]:
                dfs(node)
            return
        vis = set()
        for i in range(n):
            if i not in vis:
                provinces += 1
                dfs(i)
        return provinces