class Solution:
    def reverseVowels(self, x: str) -> str:
      s = [i for i in x]
      sett = {"a","e","i","o","u"}
      l = 0 
      r = len(s) - 1
      while l < r:
        if s[l].lower() in sett and s[r].lower() in sett:
          s[l], s[r] = s[r], s[l]
          l += 1
          r -= 1
        while l < r and s[l].lower() not in sett:
          l += 1
        while l < r and s[r].lower() not in sett:
          r -= 1
      ans = "".join(s)
      return ans
        
        
        