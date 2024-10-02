class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        maxi = primeOne * primeTwo
        dp = [0] * (maxi + 1)
        dp[primeOne] = 1
        dp[primeTwo] = 1
        for i in range( len(dp)):
            if i - primeTwo >= 0 and dp[i - primeTwo] == 1:
                dp[i] = 1
            if i - primeOne >= 0 and dp[i - primeOne] == 1:
                dp[i] = 1

        # for index, value in enumerate(dp):
        #     print(index, value)
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == 0:
                return i
        return 1
                  