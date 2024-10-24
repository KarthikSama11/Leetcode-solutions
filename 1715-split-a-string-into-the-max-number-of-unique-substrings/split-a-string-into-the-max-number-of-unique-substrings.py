class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        subs =set()
        def dfs(subs, i):
            if i == N:
                return 0
            # print(subs)
            ans = 0
            for j in range(i, N):
                word = s[i : j + 1]
                if word in subs:
                    continue
                if len(subs) + N - j <= ans:
                    return ans
                subs.add(word)
                ans = max(ans,dfs(subs, j + 1)+1)
                subs.remove(word)
            return ans
        return dfs(subs, 0)
            