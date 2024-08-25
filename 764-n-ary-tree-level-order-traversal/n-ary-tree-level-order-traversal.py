"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      q = deque()
      ans = []
      node = root
      if not root:
        return []
      q.append(node)
      while len(q) > 0:      
        level = []
        size = len(q)
        while size:
          node = q.popleft()
          level.append(node.val)
          for child in node.children:
            q.append(child)
          size -= 1
          # print(level)
        ans.append(level.copy())
        # level.clear()
        
      return ans   
