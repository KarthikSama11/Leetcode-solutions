# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      def getLength(head):
        node = head
        count = 0
        while node.next is not None:
          node = node.next
          count += 1 
        return count
      dummy = ListNode(-1, head)
      N = getLength(head)
      reqLen = N // 2
      for i in range(reqLen):
        head = head.next
    
      return head if N % 2 == 0 else head.next