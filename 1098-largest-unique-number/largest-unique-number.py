class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        arr = [0] * 1001
        ans = -1
        for num in nums:
            arr[num] += 1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 1:
                return i
        return -1
        