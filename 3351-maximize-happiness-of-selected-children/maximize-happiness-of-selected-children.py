class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
      picked = 0
      happiness.sort()
      ans = 0
      for i in range(len(happiness) - 1, -1, -1):
        #print(ans)
        if k > 0:
          ans += max(0,happiness[i] - picked)
          picked += 1
          k -= 1
      return ans

      