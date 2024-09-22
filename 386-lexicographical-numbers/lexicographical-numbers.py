class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
      res = []
      def dfs(num):
        if num < 1 or num > n:
          return
        # print(num, n)
        res.append(num)
        num *= 10
        for i in range(0, 10):
          if num + i > n:
            return
          dfs(num + i)
        return
      for i in range(1, 10):
        dfs(i)
      # print(res)
      return res