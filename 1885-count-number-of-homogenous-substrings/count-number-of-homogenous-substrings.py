class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        count = 0
        mod = 1e9 + 7
        for i, c in enumerate(s):
            if i > 0 and s[i - 1] != s[i]:
                count = 0
            count = (count + 1) % mod
            ans =  (ans + count) % mod
            print(count, ans)
        return int(ans)