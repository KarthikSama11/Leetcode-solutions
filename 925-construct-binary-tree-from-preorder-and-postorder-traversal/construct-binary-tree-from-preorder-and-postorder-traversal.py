# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # root = TreeNode(pre[0])
        dummy = TreeNode(0)
        def recurse(pre, post):
            if len(pre) == 0:
                return None
            if len(pre) == 1:
                return TreeNode(pre[0])
            root = TreeNode(pre[0])
            if pre[1] != post[-2]:
                prelimit = len(pre)
                for i in range(1, len(pre)):
                    if pre[i] == post[-2]:
                        prelimit = i
                        break
                
                postlimit = 0
                for j in range(len(post) - 2, -1, -1):
                    if post[j] == pre[1]:
                        postlimit = j
                        break
                # print(count)
                a = pre[1:prelimit ]
                b = post[postlimit+1:len(post) - 1]
                c = pre[prelimit:]
                d = post[0: postlimit + 1]
                # print(a,d)
                # print(c, b)
                root.left = recurse(a, d)
                root.right = recurse(c, b)

            else:
                root.left = recurse(pre[1:], post[0:len(post) - 1])
            return root
        dummy.left = recurse(preorder, postorder)
        return dummy.left

        #     1
        # 3       2
        #     4
    

