# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
      xvals = [None, -1]
      yvals = [None, -2]
      def dfs(node, parent = None, level = 0):
        if not node:
          return
        if node.val == x:
          xvals[0] = parent
          xvals[1] = level
        elif node.val == y:
          yvals[0] = parent
          yvals[1] = level
        print(node.val)
        dfs(node.left , node, level + 1)
        dfs(node.right, node, level + 1)
        return
      dfs(root, None, 0)
      print(xvals,yvals)
      return True if xvals[0] != yvals[0] and xvals[1] == yvals[1] else False

