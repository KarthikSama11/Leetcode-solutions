# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.flips = 0
        if not root1 and not root2:
            return True
        def dfs(p, q):
            if p and not q:
                return False
            if not p and q:
                return False
            if not p and not q:
                return True
            if p.val !=  q.val:
                return False
            if p.val == q.val and not p.left and not q.left and not p.right and not q.right:
                return True
            a,b,c,d = False, False, False, False

            a = dfs(p.left, q.left)
            b = dfs(p.right, q.right)
            c = dfs(p.left, q.right)
            d = dfs(p.right, q.left)

            return (a and b) or( c and d)
        return dfs(root1, root2)

            