# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      def dfs(node, ans):
        if not node:
          return
        dfs(node.left, ans)
        dfs(node.right, ans)
        ans.append(node.val)
        return
      ans = []
      dfs(root,ans)
      return ans
