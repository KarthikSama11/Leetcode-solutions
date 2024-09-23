class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(reverse =True)
        s = set(words)
        bestword = ""
        bestlen = 0
        for word in words:
            size = len(word)
            for j in range(size):
                if word[:j+1] not in s:
                    break
                elif j + 1 > bestlen:
                    bestword = word
                    bestlen = j + 1
                elif j + 1 == bestlen:
                    bestword = min(bestword, word)
        return bestword
                    

        
