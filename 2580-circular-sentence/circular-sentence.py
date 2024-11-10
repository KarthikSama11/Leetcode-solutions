class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        ans = True
        for i in range(1, len(words)):
            if words[i - 1][-1] != words[i][0]:
                ans = False
        if words[0][0] != words[-1][-1]:
            ans = False
        return ans