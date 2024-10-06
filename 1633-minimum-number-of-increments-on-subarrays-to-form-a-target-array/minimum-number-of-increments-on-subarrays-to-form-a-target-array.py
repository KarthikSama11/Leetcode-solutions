class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev, ans = 0, 0
        for num in target:
            ans += max(0, num - prev)
            prev = num
        return ans