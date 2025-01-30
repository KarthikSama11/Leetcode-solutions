class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        ans = 0
        for c in s:
            if c == "1":
                ones += 1
        right = ones
        left = 0
        N = len(s)
        for i, c in enumerate(s):
            if c == "0":
                left += 1
            else:
                right -= 1
                right = max(0, right)
            if i < N -1:
                ans = max(ans, left + right)

        return ans