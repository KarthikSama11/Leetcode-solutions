# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
      swaps = 0
      arrays = []
      q = deque()
      q.append(root)
      while q:
        size = len(q)
        level = []
        for i in range(size):
          node = q.popleft()
          level.append(node.val)
          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)
        arrays.append(level.copy())
        level.clear()
      def minswaps(arr):
        ans = 0
        hashmap = {}
        for i in range(len(arr)):
          hashmap[arr[i]] = i 
          # (7-0) (6-1) (8-2) (5-3)
        arr.sort()
        #  5 6 7 8
        #  8 6 7 5
        #  7 6 8 5
        for i in range(len(arr)):
          while hashmap[arr[i]] != i:
            j = hashmap[arr[i]]
            arr[i],arr[j] = arr[j], arr[i]
            ans += 1

        
        return ans
      for arr in arrays:
        swaps += minswaps(arr)
      return swaps
      