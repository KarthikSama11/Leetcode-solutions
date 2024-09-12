class Solution:
    def similarPairs(self, words: List[str]) -> int:
      umap = defaultdict(int)
      ans = 0
      def nchooseR(n, r = 2):
        if n <= 1:
          return 0
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        
      for word in words:
        freq  = ['0'] * 26
        for ch in word:
          i = ord(ch) - ord('a')
          freq[i] = '1'
        code = '-'.join(freq)
        umap[code] += 1
      for key, val in umap.items():
        
        ans += nchooseR(val, 2)
      # print(umap)
      return ans