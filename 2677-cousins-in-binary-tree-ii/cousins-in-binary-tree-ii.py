# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
        return
      levelsums = defaultdict(int)
      level = 0
      q = deque()
      q.append(root)
      while q:
        size = len(q)
        # print(size)
        while size:
          rode = q.popleft()
          levelsums[level] += rode.val
          if rode.left:
            q.append(rode.left)
          if rode.right:
            q.append(rode.right)
          size -= 1
        level += 1
      # print(levelsums)

      def dfs(node = None, level = 0 ):
        if not node: 
          return
        dfs(node.left , level + 1)   
        dfs(node.right, level + 1)
        cursum = 0
        if node.left:
          cursum += node.left.val
        if node.right:
          cursum += node.right.val
        if node.left:
          node.left.val = levelsums[level+1] - cursum
        if node.right:
          node.right.val = levelsums[level + 1] - cursum
        return
      dfs(root,  0)
      root.val = 0
      return root