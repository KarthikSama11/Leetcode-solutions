class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        print(intervals)
        ans = 0
        l = 0
        for i in range(1, len(intervals)):
            if intervals[l][1] > intervals[i][0]:
                ans += 1 
            else:
                l = i
        return ans
        