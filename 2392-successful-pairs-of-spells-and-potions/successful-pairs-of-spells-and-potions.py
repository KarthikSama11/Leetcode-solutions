class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
      ans = []
      potions.sort()
      for mul in spells:
        count = 0
        l,r = 0, len(potions) - 1
        while l <= r:
          m = (l + r)//2
          if potions[m] * mul >= success:
            count = len(potions) - m
            r = m - 1
          else:
            l = m + 1
        ans.append(count)
      return ans
          
