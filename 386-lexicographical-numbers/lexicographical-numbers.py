class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
      res = [x for x in range(1, n + 1)]
      print(res)
      def mysort(item1, item2):
        return str(item1) < str(item2)
      res.sort(key = lambda x: str(x))
      return res
      # res = []
      # def dfs(num = 0):
      #   num *= 10
      #   if num > n:
      #     return
      #   for i in range(0,10):
      #     num += i
      #     # if num > 0:
      #     res.append(num)
      #     # if num <= n:
      #     dfs(num)
      #     num -= i
      # dfs(0)
      # return res
