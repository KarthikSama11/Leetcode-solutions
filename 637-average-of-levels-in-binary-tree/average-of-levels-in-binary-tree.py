# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
      ans = []
      q = deque()
      q.append(root)
      while q:
        totalsum = 0
        count, size = len(q), len(q)    
        while size:
          node = q.popleft()
          totalsum += node.val
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
          size -= 1
        ans.append(totalsum/count)
      return ans
