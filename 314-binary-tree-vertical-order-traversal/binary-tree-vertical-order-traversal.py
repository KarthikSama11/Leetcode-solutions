# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticalmap = defaultdict(list)
        ans = []
        def dfs(node, x, y):
            if not node:
                return
            # print(node.val, x)
            verticalmap[x].append((y, node.val))
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)
            return
        dfs(root, 0, 0)
        # print(verticalmap)
        def customsort(item1, item2):
            # print(item1, item2)
            if item1[0] == item2[0]:
                return 0
            elif item1[0] < item2[0]:
                return -1
            else:
                return 1
        for _, v in sorted(verticalmap.items()):
            v.sort(key = cmp_to_key(customsort))
            temp = []
            for _, value in v:
                temp.append(value)
            ans.append(temp)
            
        return ans
