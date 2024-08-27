# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
      self.hashmap = defaultdict(int)
      self.odds = 0
      self.ans = 0
      def dfs(node):
        if not node:
          return
        # if node.val in self.hashmap : 
        #   if self.hashmap[node.val] %2 == 0:
        #     self.odds += 1
        #   else:
        #     self.odds -= 1
        #   self.hashmap[node.val] += 1
        # elif node.val not in self.hashmap:
        #   self.odds += 1
        #   self.hashmap[node.val] = 1
        self.hashmap[node.val] += 1
        if not node.left and not node.right:
          odd = 0
          for k,v in self.hashmap.items():
            if v % 2 != 0:
              odd += 1
          if odd <= 1:
            self.ans += 1
          self.hashmap[node.val] -= 1
          return
        dfs(node.left)
        dfs(node.right)
        self.hashmap[node.val] -= 1
        # if self.hashmap[node.val] %2 == 0:
        #   self.odds += 1
        # else:
        #   self.odds -= 1
      dfs(root)
      return self.ans