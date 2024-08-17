class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
      if str1 + str2 != str2 + str1:
        return ""
      g = gcd(len(str1), len(str2))
      return str1[0:g]
      if len(str2) > len(str1):
        str1,str2 = str2, str1  
      ans = ""
      allPrefixes = []
      size = len(str2)
      for i in range(1, size):
        if size % i == 0:
          allPrefixes.append(str2[0: i ])
      print(allPrefixes)
      def checkPrefix(text, prefix):
        if len(text)%len(prefix)!= 0:
          return False
        i = 0
        while i <= len(text) - len(prefix):
          if text[i : i + len(prefix)] != prefix:
            return False
          i += len(prefix)
        
        return True
      if checkPrefix(str1,str2):
        # print("yes")
        return str2
      # print("np")
      for prefix in allPrefixes:
        if checkPrefix(str2,prefix):
          if checkPrefix(str1, prefix):
            ans = prefix
      if len(ans) == len(str1): 
        return ""
      return ans
