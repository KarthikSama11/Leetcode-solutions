class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        N = len(intervals)
        for i in range(1, N):
            ps, pe = res[- 1]
            cs, ce = intervals[i]
            if cs > pe:
                res.append([cs, ce])
            elif ce <= pe:
                continue
            else:
                res[-1][1] = ce
        return res