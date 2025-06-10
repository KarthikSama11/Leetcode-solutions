# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        self.__inorder(self.root)

    def __inorder(self,root):
        if not root:
            return 
        if root.left:
            self.__inorder(root.left)
        self.q.append(root.val)
        if root.right:
            self.__inorder(root.right)
        return 

    def next(self) -> int:
        if self.hasNext:
            return self.q.popleft()

    def hasNext(self) -> bool:
        return len(self.q) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()