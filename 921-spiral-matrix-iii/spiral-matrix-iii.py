class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
      totalcells = rows * cols
      ans = []
      vis = set()
      directions = [
        (0,  1),
        (1,  0),
        (0, -1),
        (-1, 0)
      ]
      direction = -1
      r, c = rStart, cStart
      def inBounds(r, c):
        if 0 <= r < rows and 0 <= c < cols:
          return True
        return False
      while totalcells:
        if inBounds(r, c):
          totalcells -= 1
          ans.append([r, c])
        vis.add((r, c))
        direction += 1
        direction %= 4
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc
        if (nr, nc) in vis:
          direction -= 1
          direction  %= 4
          dr, dc = directions[direction] 
          nr, nc = r + dr, c + dc
        r, c = nr, nc
      
      return ans