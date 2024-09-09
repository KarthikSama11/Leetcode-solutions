# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
      vis = set()
      directions = [
        (0,  1),
        (1,  0),
        (0, -1),
        (-1, 0)
      ]
      ans = [[-1 ] * n for _ in range(m)]
      # print(len(ans), len(ans[0]))
      # print("--------------------")
      x , y = 0, 0
      direction = 0
      def isvalid(x, y):
        if x < 0 or x >= m or y < 0 or y >= n:
          return False
        if ans[x][y] != -1:
          return False
        return True
      cur = head
      while cur:
        # print(x,y)
        # print( cur.val)
        ans[x][y] = cur.val
        cur = cur.next
        dx, dy = directions[direction]
        if not isvalid(x + dx, y + dy):
          direction += 1
          direction %= 4
          dx, dy = directions[direction]
        x += dx
        y += dy
      return ans