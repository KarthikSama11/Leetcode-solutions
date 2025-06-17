class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        minsofar = nums[0]
        for i in range(1, len(nums)):
            dif = nums[i] - minsofar
            res = max(res, dif)
            minsofar = min(minsofar, nums[i])
        return -1 if res <= 0 else res
