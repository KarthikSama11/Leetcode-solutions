# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
      ans = []
      def dfs(node, level):
        if not node:
          return
        if len(ans) == level:
          ans.append([])
        if node.left:
          dfs(node.left, level + 1)
        if node.right:
          dfs(node.right, level + 1)
        # print(level, node.val, ans)
        ans[level].append(node.val)
        return
      dfs(root, 0)
      ans.reverse()
      return ans

          