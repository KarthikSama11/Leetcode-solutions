class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      arr = sorted(heights)
      # sort(arr)
      ans = 0
      for i in range(len(heights)):
        if arr[i] != heights[i]:
          ans += 1
      return ans