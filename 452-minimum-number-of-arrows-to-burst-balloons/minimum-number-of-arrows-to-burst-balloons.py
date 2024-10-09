from functools import cmp_to_key
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        if len(points) <= 1:
            return len(points)
        def compare(a, b):
            if a[1] < b[1]:
                return -1
            else:
                return 1
        points = sorted(points, key = cmp_to_key(compare))
        # print(points)
        gun = points[0][1] 
        for s, e in points:
            # print(gun)
            if gun < s:
                ans += 1
                gun = e
        return ans