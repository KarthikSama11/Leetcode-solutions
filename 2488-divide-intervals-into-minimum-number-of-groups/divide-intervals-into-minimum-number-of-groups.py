from sortedcontainers import SortedDict
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        # intervals.sort(key = lambda x: x[1])
        line = SortedDict()
        for s,e in intervals:
            if s not in line:
                line[s] = 0
            if e + 1 not in line:
                line[e + 1] = 0
            line[s] += 1
            line[e + 1] -= 1
        cnt = 0
        ans = 1
        for _, v in line.items():
            cnt += v
            ans = max(ans, cnt)
        return ans