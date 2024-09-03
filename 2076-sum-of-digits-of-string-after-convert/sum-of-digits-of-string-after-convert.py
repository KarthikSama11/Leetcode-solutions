class Solution:
    def getLucky(self, s: str, k: int) -> int:
      def chartonum(bet):
        if not bet.isalpha():
          return 0

        val = ord(bet.lower()) - ord('a') + 1
        res = 0
        while val:
          res += val % 10
          val //= 10
        
        return res
      ans = 0
      for ch in s:
        ans += chartonum(ch)
      k -=1
      def numtonum(num):
        ans = 0
        while num:
          ans += num % 10
          num //= 10
        return ans
      while k:
        ans = numtonum(ans)
        k -= 1
      return ans


          
        