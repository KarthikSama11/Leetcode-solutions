class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
      
      arr = []
      ans = 24 * 60
      for time in timePoints:
        tup = int(time[0: 2]) * 60 + int(time[3: 5])
        arr.append(tup)
      arr.sort()
      arr.append(arr[0] + 24 * 60)
      print(arr)
      for i in range(1, len(arr)):
        ans = min(ans, arr[i] - arr[ i - 1])
      return ans
      
      