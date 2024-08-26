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

      def dfs(p, q):
        if not p and not q:
          return True
        if not p and q:
          return False
        if not q and p:
          return False
        if p.val != q.val:
          return False 
        l = dfs(p.left, q.left)
        r = dfs(p.right, q.right)
        return l and r
      
      return dfs(p, q) 
           