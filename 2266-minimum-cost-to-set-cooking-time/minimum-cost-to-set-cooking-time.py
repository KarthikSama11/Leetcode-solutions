class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
      ans = 1e9
      def getCost(arr, prev = startAt):
        a,b,c,d = tuple(arr)
        # if a == 1 and b== 0 and c == 0 and d == 0:
        #   print()

        returnVal = 0
        initial = 0
        while arr[initial] == 0:
          initial += 1
        for i in range(initial, len(arr)):
          if prev != arr[i]:
            returnVal += moveCost
          returnVal += pushCost
          prev = arr[i]
        return returnVal

      for minutes in range(0, 100):
        mm = minutes * 60
        if mm > targetSeconds:
          break
        ss = targetSeconds - mm
        if ss > 99:
          continue
        time = [0,0,0,0]
        mm = str(minutes)
        ss = str(ss)
        # print(mm, ss)
        if len(mm) == 2:
          time[0] = int(mm[0])
          time[1] = int(mm[1])
        else:
          time[1] = int(mm)
        if len(ss) == 2:
          time[2] = int(ss[0])
          time[3] = int(ss[1])
        else:
          time[3] = int(ss)
        value = getCost(time)
        ans = min(ans, value)


      return ans