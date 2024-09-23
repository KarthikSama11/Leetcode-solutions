class Solution:
    def lexicalOrder(self, N: int) -> List[int]:
      res = []
      # def dfs(num):
      #   if num < 1 or num > n:
      #     return
      #   # print(num, n)
      #   res.append(num)
      #   num *= 10
      #   for i in range(0, 10):
      #     dfs(num + i)
      #   return
      # for i in range(1, 10):
      #   dfs(i)
      digits = len(str(N))
      start = 10 ** (digits - 1)
      end = 10 ** digits
      print(start, end)
      for i in range(start, end):
        current = []
        current.append(i)
        while i % 10 == 0:
          i //= 10
          current.append(i)
        res.extend(j for j in current[::-1] if j <= N)
      return res