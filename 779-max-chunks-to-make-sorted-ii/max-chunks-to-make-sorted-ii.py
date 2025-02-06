class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        chunks = 0
        # if len(arr):
        #     stack.append(arr[0])
        for i, num in enumerate(arr):
            if not len(stack) or stack[-1] <= num:
                stack.append(num)
                continue
            maxi = num
            while len(stack) and stack[-1] > num:
                maxi = max(maxi, stack.pop())
            stack.append(maxi)
                
            
            
        print(stack)
            
        return len(stack)