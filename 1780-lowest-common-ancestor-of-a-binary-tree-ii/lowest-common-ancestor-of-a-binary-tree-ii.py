# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pfound = False
        qfound = False
        def dfs(node):
            nonlocal pfound
            nonlocal qfound
            if not node:
                return None
            l = dfs(node.left)
            r = dfs(node.right)
            if node == p:
                pfound = True
            if node == q:
                qfound = True
            if (l==p or r==p) and (l == q or r == q):
                return node
            if node == p or node == q:
                return node
            return l or r
        ans = dfs(root)
        if not pfound or not qfound:
            return None
        return ans