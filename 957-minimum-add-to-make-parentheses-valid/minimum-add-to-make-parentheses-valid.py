class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        cnt = 0
        for par in s:
            if par == "(":
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                ans += 1
        return ans + cnt