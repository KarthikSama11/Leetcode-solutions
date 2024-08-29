# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      ans = []
      q = []
      q.append(root)
      odd = False
      while len(q):
        q1 = []
        # print(q)
        for i in range(len(q)):
          if odd and i < len(q)/2:
            q[i].val,q[len(q) - 1 - i].val =q[len(q) - 1 - i].val, q[i].val 
          if q[i].left:
            q1.append(q[i].left)
          if q[i].right:
            q1.append(q[i].right)
        
        q = q1
        odd = not odd
      return root
