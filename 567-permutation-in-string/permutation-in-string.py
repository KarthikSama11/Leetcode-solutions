class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26
        for i, ch in enumerate(s1):
            j = ord(ch) - ord('a')
            f1[j] += 1
        # print('-',f1)

        for i, ch in enumerate(s2):
            r = ord(ch) - ord('a')
            if i >= len(s1):
                l = ord(s2[i - len(s1)]) - ord('a')
                f2[l] -= 1
            f2[r] += 1
            if f1 == f2:
                return True
        return False
