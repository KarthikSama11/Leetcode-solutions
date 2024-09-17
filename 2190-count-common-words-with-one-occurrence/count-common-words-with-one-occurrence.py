class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
      m1, m2 = Counter(words1), Counter(words2)
      ans = 0
      for k, v in m1.items():
        if v > 1:
          continue
        if k in m2 and m2[k] == 1:
          ans += 1
      return ans 
         