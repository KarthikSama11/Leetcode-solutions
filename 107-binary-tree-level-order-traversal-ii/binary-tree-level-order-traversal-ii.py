# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
      ans = []
      if not root:
        return []
      q = deque()
      q.append(root)
      while q:
        size = len(q)
        level = []
        while size:
          node = q.popleft()
          level.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
          size -= 1
        ans.append(level.copy())
      ans.reverse()
      return ans
          