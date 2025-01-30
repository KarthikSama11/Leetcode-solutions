class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countzeroes = 0
        ans = 0
        for i, c in enumerate(s):
            if c == "R":
                countzeroes += 1
            else :
                countzeroes -= 1
            ans += 1 if countzeroes == 0 else 0
        return ans