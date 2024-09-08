# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
      ans = []
      n = 0
      start = head
      while start is not None:
        start = start.next
        n += 1
      def dfs(head, size):
        dummy = ListNode(-1,head)
        # dummy.next = head
        cur = dummy
        for i in range(size):
          cur = cur.next
        nexthead = cur.next
        cur.next = None
        print(dummy.next, nexthead)
        return (dummy.next, nexthead)

      while k :
        # if n == 0:
        #   ans.append()
        #   k -= 1
        #   continue

        requiredlen = n//k
        if n % k != 0:
          requiredlen += 1
        n -= requiredlen
        blockhead, head = dfs(head, requiredlen)
        ans.append(blockhead)
        k -= 1

      return ans