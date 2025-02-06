class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        pre = 0
        cur = 0
        ans = 0
        for i, num in enumerate(arr):
            pre += i
            cur += num
            if pre == cur:
                ans += 1
        return ans