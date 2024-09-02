# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
      self.target = None
      self.dad = {}
      def finder(node):
        if not node:
          return
        if node.val == start:
          # print(start)
          self.target = node
          # print(node.val)
        if node.left:
          self.dad[node.left] = node
          finder(node.left)
        if node.right:
          self.dad[node.right] = node
          finder(node.right)
      finder(root)
      # print(self.target)
      minutes = 0
      q = deque()
      q.append(self.target)
      vis = set()
      while q:
        q1 = deque()
        # print(q)
        # print("\n")
        for i in range(len(q)):
          node = q.popleft()
          vis.add(node)
          if node in self.dad and self.dad[node] not in vis:
            q1.append(self.dad[node])
          if node.left and node.left not in vis:
            q1.append(node.left)
          if node.right and node.right not in vis:
            q1.append(node.right)
        q = q1
        if len(q):
          minutes += 1
        else:
          break
      return minutes
