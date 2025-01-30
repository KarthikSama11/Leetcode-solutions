class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = [0] * 26
        ans = 0
        for c in s:
            ind = ord(c) - ord('a')
            ans += freq[ind] + 1
            freq[ind] += 1
        return ans