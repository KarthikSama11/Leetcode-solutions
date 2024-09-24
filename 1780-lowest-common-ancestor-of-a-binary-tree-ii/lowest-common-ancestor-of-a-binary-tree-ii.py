# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pfound = False
        self.qfound = False
        def dfs(node):
            # nonlocal pfound
            # nonlocal qfound
            if not node:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node == p:
                self.pfound = True
            if node == q:
                self.qfound = True
            if (l==p or r==p) and (l == q or r == q):
                return node
            if node == p or node == q:
                return node
            return l or r
        ans = dfs(root)
        if not self.pfound or not self.qfound:
            return None
        return ans