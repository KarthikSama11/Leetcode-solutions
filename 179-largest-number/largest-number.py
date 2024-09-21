class Solution:
    def largestNumber(self, nums: List[int]) -> str:
      arr = [str(x) for x in nums]
      def my_comp(s1, s2):
        # print(s1,s2, s1 + s2, s2 + s1, s1 > s2)
        if s1 + s2 > s2 + s1:
          return -1
        return 1

      arr = sorted(arr, key = cmp_to_key(my_comp))
      res = "".join(arr)
      start = 0
      while  start < len(res) and res[start] == "0" :
        start += 1
      res = res[start:]
      if len(res):
        return res

      return "0"

