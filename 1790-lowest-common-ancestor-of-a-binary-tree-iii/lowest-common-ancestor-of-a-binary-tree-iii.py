"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #looks very much like intersection of linked lists
        prr, qrr = [], []
        while p:
            prr.append(p)
            p = p.parent
        while q:
            qrr.append(q)
            q = q.parent
        # print(prr, qrr)
        size = min(len(prr), len(qrr))
        l = -1
        r = -1
        ans = None
        for i in range(size):
            if prr[l].val == qrr[r].val:
                ans = prr[l]
                l -= 1
                r -= 1
        return ans