# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      def dfs(p,q):
        if not p and not q:
          return True
        if (not p and q) or (not q and p) or (p.val != q.val):
          return False
        l = dfs(p.left, q.right)
        r = dfs(p.right, q.left)
        return l and r
      return dfs(root.left, root.right)
   