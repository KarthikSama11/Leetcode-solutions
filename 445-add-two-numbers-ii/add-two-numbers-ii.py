# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      def reverselist(node):
        prev = None 
        cur = node
        cnt = 0
        while cur:
          nextnode = cur.next
          cur.next = prev
          prev = cur
          cur = nextnode
          cnt += 1
        return (prev, cnt)
      print(l1, l2)
      l1, cnt1 = reverselist(l1) 
      l2, cnt2 = reverselist(l2)
      carry = 0
      if cnt1 < cnt2:
        d1, d2 = l2, l1
      else:
        d1, d2 = l1, l2
      print(d1, d2)
      while d1:
        newval = d1.val  + carry
        if d2:
          newval += d2.val  
        carry= newval//10
        newval %= 10
        d1.val = newval
        if carry > 0 and not d1.next:
          d1.next = ListNode(carry)
          break
        d1 = d1.next
        if d2:
          d2 = d2.next
      ans, c = reverselist(l1) if cnt1 >= cnt2 else reverselist(l2)
      return ans

