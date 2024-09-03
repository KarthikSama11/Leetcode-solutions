class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
      ans = 0
      # pre = 0
      # for i in range(len(chalk)):
      #   pre += chalk[i]
      #   chalk[i] = pre
      # if pre < k:
      k = k%sum(chalk)
      # print(k)
      for i in range(len(chalk)):
        k -= chalk[i]
        if k < 0:
          return i
      # l,r = 0, len(chalk) - 1
      # while l <= r:
      #   mid = l + r
      #   mid /= 2
      #   if chalk[mid] < k:
      #     l = mid + 1
      #   elif chalk[mid] == k:
      #     return mid
      #   elif chalk[mid] > k:

      return 0