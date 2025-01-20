class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        numrows = len(mat)
        numcols = len(mat[0])
        nummap = {}
        for r in range(numrows):
            for c in range(numcols):
                nummap[mat[r][c]] = (r,c)
        order = []
        for value in arr:
            order.append(nummap[value])
        
        rows = [numcols] * numrows
        cols = [numrows] * numcols
        # print(rows)
        # print(cols)
        for i in range(len(order)):
            r,c = order[i]
            rows[r] -= 1
            if rows[r] == 0:
                return i
            cols[c] -= 1
            if cols[c] == 0:
                return i
        return len(arr) 