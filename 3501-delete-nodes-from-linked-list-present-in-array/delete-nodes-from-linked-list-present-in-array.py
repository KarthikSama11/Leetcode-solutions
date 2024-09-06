# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
      hashset = set(nums)
      dummy =   ListNode(0, head)
      # print(dummy)
      cur = dummy
      # print(hashset)
      while cur:
        print(cur.val, cur.val in hashset)
        # if cur.next and cur.next.val not in hashset:
        #   cur = cur.next
        #   continue
        while cur.next and cur.next.val in hashset:
          # print(cur, cur.next, cur.next.next)
          cur.next = cur.next.next
        cur = cur.next
        
      return dummy.next