# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      self.pvals = []
      self.qvals = []

      def dfs(node, arr):
        if not node:
          arr.append(-1e5)
          return 

        dfs(node.left, arr)
        dfs(node.right, arr)
        arr.append(node.val)
        return
      dfs(p, self.pvals)
      dfs(q, self.qvals)
      print(self.pvals, self.qvals)
      return self.pvals == self.qvals  
           