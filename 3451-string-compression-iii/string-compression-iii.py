class Solution:
    def compressedString(self, word: str) -> str:
        cnt = 1
        comp = ""
        N = len(word)
        for i in range(N):
            if i + 1 < N and word[i] == word[i + 1] and cnt < 9:
                cnt += 1
                
            else:
                # times = cnt // 9
                # for j in range(times):
                #     comp += str(9) + word[i]
                # times = cnt % 9
                # if times > 0:
                comp += str(cnt) + word[i]
                cnt = 1
        return comp
            