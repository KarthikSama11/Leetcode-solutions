# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      ans = []
      q = deque()
      node = root
      if not root:
        return []
      q.append(root)
      direction = True
      # levels = 0
      while q:
        size = len(q)
        level = [0]*size
        i = 0
        while i < size:
          node = q.popleft()
          idx = i if direction  else size - 1 -i
          level[idx] = node.val
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
          # size -= 1 
          i += 1
        # if levels % 2 != 0:
          # level.reverse()
        # print(level)
        ans.append(level.copy())
        level.clear()
        # levels += 1
        direction = not direction
      return ans
        
