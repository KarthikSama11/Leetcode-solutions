class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
      s = bin(start)[2:]
      # print(s)
      g = bin(goal)[2:]
      if len(g) > len(s) :
        return self.minBitFlips(goal,start)
      i = 0
      print(s, g)
      ans = 0
      i = -1
      while -i <= len(s):
        if -i <= len(g):
          if g[i] != s[i]:
            ans += 1
        else:
          if s[i] == '1':
            ans += 1
        i -= 1
      return ans
      while i < len(g) :
        print(g[len(g) - i - 1], s[len(s) - i - 1])
        if g[len(g) - i - 1] != s[len(s) - i - 1]:
          ans += 1
        i += 1
      if len(s) == len(g):
        return ans
      for j in range(len(s) - len(g) + 1):
        # print(s[j])
        if s[j] == '1':
          # print("hi",s[j])
          ans += 1
      return ans