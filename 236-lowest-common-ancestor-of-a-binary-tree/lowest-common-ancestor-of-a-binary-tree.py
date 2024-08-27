# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      self.ans = -1
      def dfs(node):
        if not node:
          return 0
        left = dfs(node.left)
        right = dfs(node.right) 
          
        if (node.val == p.val or node.val == q.val) and (left == 1 or right == 1):
          self.ans = node
        elif left == 1 and right == 1:
          self.ans = node
        if node.val == p.val or node.val == q.val:
          return 1
        
        return left or right
      dfs(root)
      print(self.ans)
      return self.ans