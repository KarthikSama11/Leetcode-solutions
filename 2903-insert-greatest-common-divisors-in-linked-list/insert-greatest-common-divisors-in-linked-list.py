# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
      left = head
      right = head.next
      # def gcd(a, b):
        
      while right:
        newVal = math.gcd(min(left.val, right.val), max(left.val, right.val))
        newNode = ListNode(newVal, right)
        left.next = newNode
        left = right
        right = right.next

      return head    