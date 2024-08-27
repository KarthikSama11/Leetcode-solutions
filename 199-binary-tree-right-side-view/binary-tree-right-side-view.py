# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      ans = []
      q = deque()
      if not root:
        return []
      q.append(root)
      while q:
        size = len(q)
        q1 = deque()
        ans.append(q[-1].val)
        for i in range(len(q)):
          node = q.popleft()  
          # if len(q) == 0:
          #   ans.append(node.val)
          if node.left:
            q1.append(node.left)
          if node.right:
            q1.append(node.right)
        q = q1
      return ans 