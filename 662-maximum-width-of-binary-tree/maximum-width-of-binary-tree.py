# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      ans = 0
      if not root:
        return ans
      q = deque()
      q.append((root,0))
      while q:
        q1 = deque()
        curwidth = q[-1][1] - q[0][1] + 1
        ans = max(ans, curwidth)
        for i in range(len(q)):
          node, idx = q.popleft()
          if node.left:
            q1.append((node.left, 2 * idx + 1))
          if node.right:
            q1.append((node.right, 2 * idx + 2))
        q = q1
      return ans
