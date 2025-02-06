class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = [arr[0]]
        N = len(arr)
        for i in range(1, N):
            num = arr[i]
            big = num
            while len(stack) and stack[-1] > num:
                big = max(big, stack.pop())
            stack.append(big)
        return len(stack)