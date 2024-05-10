class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
      picked = 0
      happiness.sort(reverse = True)
      ans = 0
      for i in range(len(happiness)):
        if k > 0:
          ans += max(0,happiness[i] - i)
          k -= 1
      return ans

      