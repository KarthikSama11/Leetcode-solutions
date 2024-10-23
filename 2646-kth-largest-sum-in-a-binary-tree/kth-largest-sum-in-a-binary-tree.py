# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        sums = []
        heapify(sums)
        q = deque()
        q.append(root)
        while q:
            q1 = deque()
            cur = 0
            for i in range(len(q)):
                node = q.pop()
                cur += node.val
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            q = q1
            heappush(sums,cur)
            if len(sums) > k:
                heappop(sums)
        if len(sums) < k:
            return -1
        # heapify(sums)
        
        return heappop(sums)
