class Solution:
    def beautySum(self, s: str) -> int:
        # freq = [0] * 26
        N = len(s)
        ans = 0
        for i in range(N):
            freq = [0] * 26
            for j in range(i, N):
                ind = ord(s[j]) - ord('a')
                freq[ind] += 1
                if j > i and i < N - 1:
                    mini = 600
                    maxi = 0
                    for num in freq:
                        if num > 0:
                            mini = min(num, mini)
                        maxi = max(num, maxi)
                    ans += max(0, maxi - mini)
                    # print(freq, maxi, mini, ans)
        return ans   