# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list1 is None :
        return list2
      if list2 is None:
        return list1

      d1, d2 = ListNode(-1, list1), ListNode(-1, list2)
      l1, l2 = d1, list2

      while l1 and l2:
        if l1.next and l1.next.val < l2.val:
          l1 = l1.next
        else:
          temp1 = l1.next
          temp2 = l2.next
          l1.next = l2
          l2.next = temp1
          l2 = temp2
      
      return d1.next