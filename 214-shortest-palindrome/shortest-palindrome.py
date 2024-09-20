class Solution:
    def shortestPalindrome(self, s: str) -> str:
      #rabin karp
      # two variables with inverse multiplication order
      base = 29
      prefix, suffix = 0, 0
      mod = 10**9 + 7
      fix = 0
      pw = 1 
      for i, ch in enumerate(s):
        print(prefix, suffix)
        value = ord(ch) - ord('a') + 1
        prefix = (prefix* 29) % mod
        prefix =(prefix + value*29) % mod
        pw = pw * 29
        suffix =(suffix + value * pw ) % mod
        if prefix == suffix:
          fix = i
      tmp = s[fix + 1::] 
      tmp = tmp[::-1]
      return tmp + s