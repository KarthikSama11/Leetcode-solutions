class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if len(s1) < len(s2):
            return self.areSentencesSimilar(sentence2, sentence1)
        l = 0
        r = 0
        N1, N2 = len(s1), len(s2)
        while l < N2 and s1[l] == s2[l]:
                l += 1
        while r < N2 and s1[N1 - 1 - r] == s2[N2 - 1 - r]:
                r += 1

        return l + r >= N2

        
        