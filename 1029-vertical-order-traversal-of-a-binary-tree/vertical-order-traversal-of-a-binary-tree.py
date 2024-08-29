# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
      ans = []
      self.hashmap = defaultdict(list)
      def dfs(node, x = 0, y = 0):
        if not node:
          return
        self.hashmap[y].append( (x,node.val)) 
        dfs(node.left , x + 1, y - 1)
        dfs(node.right, x + 1, y + 1)
      dfs(root)
      # print(self.hashmap.items())
      # print(sorted(self.hashmap.items()))
      for k,v in sorted(self.hashmap.items()):
        arr = []
        for a,b in sorted(v, key = lambda x: (x[0],x[1])):
          arr.append(b)
        ans.append(arr.copy())
        arr.clear()
      return ans

      
