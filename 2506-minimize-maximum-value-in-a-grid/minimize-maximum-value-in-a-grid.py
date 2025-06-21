class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        minheap = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                minheap.append((grid[r][c], r,c))
        highinrow = [0]*len(grid)
        highincol = [0]*len(grid[0])
        heapify(minheap)
        while minheap:
            _, row,col = heappop(minheap)
            # print(highinrow, highincol)
            grid[row][col] = max(highinrow[row], highincol[col]) + 1
            highinrow[row] = grid[row][col]
            highincol[col] = grid[row][col]
        return grid