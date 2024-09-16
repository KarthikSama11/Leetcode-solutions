class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
      arr = [False] * (24*60*2)
      for time in timePoints:
        minutes = 60*(int(time[:2])) + int(time[3:])
        if arr[minutes] == True:
          return 0
        arr[minutes] = True
        arr[minutes + 1440] = True
      prev = -1e9
      ans = 1e9
      for i in range(0, len(arr)):
        if not arr[i]:
          continue
        ans = min(ans, i - prev)
        prev = i
      return ans


        
        
        