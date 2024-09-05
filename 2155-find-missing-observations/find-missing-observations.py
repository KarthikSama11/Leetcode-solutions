class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
      totrequired = mean * (n + len(rolls)) - sum(rolls)
      if not n <= totrequired <= 6 * n:
        return []
      ans = [1] * n
      totrequired -= n
      for i in range(len(ans)):
        ans[i] += min(5, totrequired)
        totrequired += 1
        totrequired -= ans[i]
      return ans