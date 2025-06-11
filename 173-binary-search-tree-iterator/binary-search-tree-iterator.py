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
        self.stack = [root]
        self.__pushallleftnodes(root)

    def __inorder(self,root):
        # if not root:
        #     return 
        # if root.left:
        #     self.__inorder(root.left)
        # self.q.append(root.val)
        # if root.right:
        #     self.__inorder(root.right)
        # return 
        pass
    def __pushallleftnodes(self,node):
        # self.stack.append(node)
        while node.left is not None:
            node = node.left
            self.stack.append(node)

    def next(self) -> int:
        # if self.hasNext():
        #     return self.q.popleft()
        if not len(self.stack):
            return -1
        
        node = self.stack.pop()
        res = node.val
        if node.right:
            self.stack.append(node.right)
            self.__pushallleftnodes(node.right)
        return res


    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()