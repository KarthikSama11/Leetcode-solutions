class Solution:
    def longestWord(self, words: List[str]) -> str:
        bestlen = 0
        bestword = ""
        sett = set(words)
        for word in words:
          size = len(word)
          for j in range(size):
            if word[:j + 1] not in sett:
              break
            elif j + 1 > bestlen:
              bestlen = j + 1
              bestword = word
            elif j + 1 == bestlen:
              bestword = min(word, bestword)
        return bestword
