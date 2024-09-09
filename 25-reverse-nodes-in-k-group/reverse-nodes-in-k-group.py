# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      # dummy = ListNode(-1, head)
      returnNode = None
      def getLength(head):
        count = 0
        node = head
        while node:
          count += 1
          node = node.next
        return count 
      N = getLength(head)
      units, remainder = divmod(N, k)
      def reverseList(head):
        prev = None
        node = head
        tail = head
        for i in range(k):
          temp = node.next
          node.next = prev
          prev = node
          node = temp
        # tail.next = node
        return (prev, tail, node)
      gentail = None
      returnablenode = None
      for i in range(units):
        h, t, head = reverseList(head)
        if not returnablenode:
          returnablenode = h
        if gentail:
          gentail.next = h
        gentail = t
        if i == units - 1:
          gentail.next = head 
      return returnablenode