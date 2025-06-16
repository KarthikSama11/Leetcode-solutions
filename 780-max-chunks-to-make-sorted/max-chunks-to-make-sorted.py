class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int: 
        i = 0
        N = len(arr)
        chunks = 0
        while i < N:
            minimum = arr[i]
            maximum = arr[i]
            for j in range(i, N):
                minimum = min(minimum, arr[j])
                maximum = max(maximum, arr[j])
                if i == minimum and j == maximum :
                    chunks += 1
                    i = j + 1
        return chunks
                
            
            




