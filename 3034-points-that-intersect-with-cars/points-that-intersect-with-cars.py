class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cars = defaultdict(int)
        left = 1e9
        right = -1e9
        for start, end in nums:
            cars[start] += 1
            cars[end + 1] -= 1
            left = min(left, start)
            right = max(right, end + 1)
        # print(cars)
        count = 0
        ans = 0
        for i in range(left, right):
            count += cars[i]
            if count > 0:
                ans += 1
        return ans
      