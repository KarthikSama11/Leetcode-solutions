class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(row, col):
            if (row, col) in dp:
                return dp[(row, col)]
            if  row == m - 1 and col == n - 1:
                return 1
            if row >= m or col >= n:
                return 0    
            bottom = dfs(row + 1, col)
            right = dfs(row, col + 1)
            dp[(row, col)] = bottom + right
            return bottom + right
        return dfs(0,0)
