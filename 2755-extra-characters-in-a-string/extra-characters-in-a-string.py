class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
      res = len(s)
      dp = {}
      def dfs(string):
        # print(string)
        N = len(string)
        ans = len(string)
        if string in dp:
          return dp[string]
        for word in dictionary:
          W = len(word)
          for i in range(0, N - W + 1):
            for j in range(0, W):
              if word[j] != string[i+j]:
                break
              # print(word, j, word[j], string[i+j])
              if j == W-1 and word[j] == string[i + j]:
                # print(string[i:i+j+1], word)
                r = dfs(string[i + j + 1:])
                l = dfs(string[:i])
                ans = min(ans, l + r)
        dp[string] = ans
        return ans
      return dfs(s)