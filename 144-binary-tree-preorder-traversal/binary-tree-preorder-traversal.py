# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      ans = []
      def dfs(root):
        if not root:
          return
        ans.append(root.val)
        dfs(root.left)
        dfs(root.right)
        return
      dfs(root)
      return ans
