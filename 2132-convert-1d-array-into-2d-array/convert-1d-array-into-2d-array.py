class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
      array = [[0 for _ in range(n)] for _ in range(m)] 
      i = 0
      if n*m != len(original):
        return []
      for row in range(len(array)):
        for col in range(len(array[0])):
          array[row][col] = original[i]
          i += 1
      return array