# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode(0, head)
      allvals = []
      node = dummy
      while node:
        if node.val != 0:
          allvals.append(node.val)
        node = node.next
      maxsofar = 0
      for i in range(len(allvals) - 1, 0, -1):
        maxsofar = max(maxsofar, allvals[i])
        allvals[i] = maxsofar
      
      node = dummy
      i = 1
      print(allvals)

      while i < len(allvals):
        if not node:
          return dummy.next
        while node.next and i < len(allvals) and node.next.val < allvals[i]:
          node.next = node.next.next
          i += 1 
        node = node.next
        i += 1
      return dummy.next


