class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      ans = []
      def dfs(i, target, cur):
        if target == 0:
          ans.append(cur.copy())
          return
        if i >= len(candidates):
          return
          
        #pick
        if candidates[i] <= target:
          cur.append(candidates[i])
          dfs(i, target - candidates[i], cur)
          cur.pop()
        # not pick
        dfs(i + 1, target, cur)
        return
      cur = []
      dfs(0, target, cur)
      return ans

       