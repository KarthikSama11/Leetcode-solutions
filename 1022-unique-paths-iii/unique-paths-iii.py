class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx, sy = 0, 0
        fx, fy = 0, 0
        rows = len(grid)
        cols = len(grid[0])
        obstacles = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    sx, sy = r, c
                elif grid[r][c] == 2:
                    fx, fy = r, c
                elif grid[r][c] == -1:
                    obstacles += 1
        clearcells = rows*cols - obstacles 
        dp = {}
        vis = set()
        def dfs(r = sx,c = sy, count = 1):
            
            if r == fx and c == fy :
                return 1 if  count == clearcells else 0
            if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] == -1 or (r,c) in vis:
                return 0
            vis.add((r,c))
            top = dfs(r - 1, c, count + 1)
            right = dfs(r, c + 1, count + 1)
            left = dfs(r, c - 1, count + 1)
            bottom = dfs(r + 1, c, count + 1)
            vis.remove((r,c))
            dp[(r,c)] = top + bottom + left + right
            return dp[(r,c)]
        return dfs()

            
