class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
      freq = [False]*26
      for ch in allowed:
        ind = ord(ch)- ord('a')
        freq[ind] = True
      ans = 0
      for word in words:
        allow = True
        for ch in word:
          ind = ord(ch) - ord('a')
          if freq[ind] == False:
            allow = False
        ans += 1 if allow == True else 0
      
      return ans

          
            
          
        