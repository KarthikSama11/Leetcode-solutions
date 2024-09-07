# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
      self.ans = False
      self.cur = head
      def dfs(treenode):
        if not treenode:
          return 0
        c = 0
        if treenode.val == head.val:
          c = checknodes(treenode, head)
        l = dfs(treenode.left)
        r = dfs(treenode.right)
        return l or r or c
      def checknodes(treenode, listnode):
        if not listnode:
          self.ans = True
          return 1
        if not treenode:
          return 0
        if treenode.val != listnode.val:
          return 0
      
        l = checknodes(treenode.left, listnode.next)
        r = checknodes(treenode.right, listnode.next)
        return l or r
      return dfs(root)