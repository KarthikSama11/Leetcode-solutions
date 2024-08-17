class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
      minsofar = arrays[0][0]
      maxsofar = arrays[0][-1]
      ans = 0
      for i in range(1, len(arrays)):
        left = arrays[i][0]
        right = arrays[i][-1]
        ans = max(abs(left - maxsofar), abs(right - minsofar), ans)
        minsofar = min(minsofar, left)
        maxsofar = max(maxsofar, right)
      return ans