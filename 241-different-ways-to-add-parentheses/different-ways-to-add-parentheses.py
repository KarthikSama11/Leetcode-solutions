class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
      # express = []
      # for x, v in groupby()
      # N = len(express)
      dp = {}
      def splitter(express):
        if len(express) <= 2:
          return [int(express)]
        if express in dp:
          return dp[express]
        res = []
        for i, ch in enumerate(express):
          if ch in "*-+":
            s1 = splitter(express[:i])
            s2 = splitter(express[i + 1::])
            print(s1, s2)
            for p in s1:
              for q in s2:
                if ch == '+':
                  x = p + q
                elif ch == '-':
                  x = p - q
                else:
                  x = p * q
                res.append(x)
        dp[express] = res
        return res
      ans = splitter(expression)
      return ans 
        


