class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      w1 = s1.split(" ")
      w2 = s2.split(" ")
      s1, s2 = Counter(w1), Counter(w2)
      ans = []
      for k, v in s1.items():
        if v > 1:
          continue
        if k not in s2:
          ans.append(k)
      for k, v in s2.items():
        if v > 1:
          continue
        if k not in s1:
          ans.append(k)
      return ans
      