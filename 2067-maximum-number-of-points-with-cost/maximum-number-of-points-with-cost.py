class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
      rows = len(points)
      cols = len(points[0])
      for r in range(rows - 1):
        left, right = [points[r][0]]*cols, [points[r][cols-1]]*cols
        for c in range(1, cols):
          left[c] = max(left[c - 1] - 1, points[r][c])
        for c in range(cols -2, -1, -1):
          right[c] = max(right[c + 1] - 1, points[r][c])
        for c in range(cols):
          points[r + 1][c] += max(left[c], right[c])
      
      ans = points[rows - 1][0]
      for c in range(1, cols):
        ans = max(ans, points[rows - 1][c])
      
      return ans
