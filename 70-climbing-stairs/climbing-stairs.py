class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}
        def dfs(i):
            if  i == n:
                return 1
            if i in dp:
                return dp[i]
            one, two = 0, 0
            if i + 1 <= n:
                one = dfs(i + 1)
            if i + 2 <= n:
                two = dfs(i + 2)
            dp[i] = one + two
            return one + two
        
        return dfs(0)
        # 0 1 2 3 4 5 6 7 8
        # 0 1 