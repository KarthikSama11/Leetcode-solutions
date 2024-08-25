# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      ans = []
      q = deque()
      node = root
      if not root:
        return []
      q.append(node)
      while q:
        size = len(q)
        level = []
        while size:
          node = q.popleft()
          # print(node.val)
          level.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
          size -= 1
        # print(level)
        ans.append(level.copy())
        level.clear()
      return ans

