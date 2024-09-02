# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
      self.dad = {}
      def dfs(node):
        if not node:
          return
        if node.left:
          self.dad[node.left] = node
        if node.right:
          self.dad[node.right] = node
        dfs(node.left)
        dfs(node.right)
      dfs(root)
      # print(self.dad)
      ans = []
      vis = set()
      q = deque()
      q.append(target)
      dist = 0
      while q:
        q1 = deque()
        if dist > k  :
          break
        # print(q, dist)
        for i in range(len(q)):
          node = q.popleft()
          vis.add(node)
          if dist == k :
            ans.append(node.val)
          if node in self.dad and self.dad[node] not in vis:
            q1.append(self.dad[node])
          if node.left and node.left not in vis:
            q1.append(node.left)
          if node.right and node.right not in vis:
            q1.append(node.right)
        q = q1
        dist += 1 
      return ans

      #  create a graph of tree nodes
      
