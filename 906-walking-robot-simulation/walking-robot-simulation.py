class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
      directions = [(0,1),
       (1,0),
       (0, -1),
       (-1, 0)
       ]   
      obstacleset = set() 
      for x, y in obstacles:
        obstacleset.add((x,y))
     
      direction = 0
      ans = 0
      x = y = 0
      for command in commands:
        if command == -1:
          direction += 1
          continue
        if command == -2:
          direction -= 1
          continue
        # if direction < 0:
        #   direction += 4
        # elif direction >= 4:
        #   direction -= 4
        direction %= 4
        for k in range(command):
          dx, dy = directions[direction]
          if (x + dx, y + dy) not in obstacleset:
            x += dx
            y += dy
          else:
            break
        ans = max(ans, x *x + y*y)
      return ans
