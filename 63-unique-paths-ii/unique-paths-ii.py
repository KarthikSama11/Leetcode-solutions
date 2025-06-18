class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = {}
        def dfs(r, c):
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r,c) in dp:
                return dp[(r,c)]
            paths = dfs(r + 1, c)
            paths += dfs(r, c + 1)
            dp[(r,c)] = paths
            return paths
        return dfs(0,0)
