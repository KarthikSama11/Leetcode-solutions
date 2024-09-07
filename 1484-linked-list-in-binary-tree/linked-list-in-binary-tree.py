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
      base = 101
      mod = 1000000007
      pattern = 0
      current = head
      size = 0
      while current:
        pattern *= base
        pattern += current.val
        pattern %= mod
        size += 1
        current = current.next
      self.listhash = pattern
      shift = pow(base, size, mod)
      def dfs(treenode, treehash, prevs):
        if not treenode:
          return False
        treehash *= base
        treehash += treenode.val
        if len(prevs) >= size:
          treehash -= shift * prevs[len(prevs)-size]
        treehash %= mod
        if treehash == pattern:
          return True
        prevs.append(treenode.val)
        l = dfs(treenode.left, treehash, prevs)
        r = dfs(treenode.right, treehash, prevs)
        prevs.pop()
        return l or r
      return dfs(root, 0, [])