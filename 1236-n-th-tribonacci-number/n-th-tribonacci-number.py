class Solution:
    def tribonacci(self, n: int) -> int:
      arr = [0,1,1]
      if n == 0: return 0
      if n == 1 or n == 2: return 1
      for i in range(3,n + 1):
        val = arr[0] + arr[1] + arr[2]
        arr[0] = arr[1]
        arr[1] = arr[2]
        arr[2] = val
      return arr[2]
