# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      def dfs(node): 
        left, right = 0, 0
        if node.left:
          left += dfs(node.left)
        if node.right:
          right += dfs(node.right)
        return 1 + max(left , right)
      return  dfs(root)