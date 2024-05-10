class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
      ans = ""
      for i in range(len(word)):
        if word[i] == ch:
          for j in range(i, -1, -1):
            ans = ans + word[j]
          for j in range(i + 1, len(word)):
            ans = ans + word[j]
          return ans
      return word      