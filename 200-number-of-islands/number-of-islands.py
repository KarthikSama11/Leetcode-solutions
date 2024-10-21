class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        vis = [[0]*cols for i in range(rows)]
        ans = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        def isValid(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if grid[row][col] == "0" or vis[row][col] == 1:
                return False
            return True
        def bfs(row, col):
            if vis[row][col] == 1:
                return 0
            q = deque()
            q.append((row,col))
            while q:
                size = len(q)
                for i in range(size):
                    r, c = q.pop()
                    vis[r][c] = 1
                    for j in range(4):
                        nr = r + dx[j]
                        nc = c + dy[j]
                        if isValid(nr, nc):
                            q.append((nr, nc))
            return  1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and vis[r][c] == 0:
                    ans += bfs(r, c)
                    # bfs(r, c)
                    # print(vis)
                    # print("----------")
                

        return ans
