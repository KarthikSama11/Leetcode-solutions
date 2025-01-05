class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        N = len(s)
        suffixsum = [0] * N
        num = 0
        for i in range(N - 1, -1, -1):
            num += shifts[i]
            num %= 26
            suffixsum[i] = num
        ans = ''
        # print(suffixsum)
        for i in range(N):
            num = ord(s[i]) + suffixsum[i] - ord('a')
            # print(num)
            num%= 26
            ans = ans + chr(num + ord('a'))
            # print(ans)
        return ans