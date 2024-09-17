class Solution:
    def totalMoney(self, n: int) -> int:
      arr = [0] * 7
      pre = 0
      for i in range(0, n ):
        ind = i % 7
        print(i, ind)
        if ind == 0:
          arr[ind] += 1
        else:
          arr[ind] = arr[ind - 1] + 1
        pre += arr[ind]
      print(arr)
      return pre
