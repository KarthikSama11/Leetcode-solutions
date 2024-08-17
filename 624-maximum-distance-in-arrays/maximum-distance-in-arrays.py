class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
      smallest = arrays[0][0]
      biggest = arrays[0][-1]
      ans = 0
      for i in range(1, len(arrays)):
        left = arrays[i][0]
        right = arrays[i][-1]
        ans = max(abs(left - biggest), abs(right - smallest), ans)
        smallest = min(smallest, left)
        biggest = max(biggest, right)
      return ans