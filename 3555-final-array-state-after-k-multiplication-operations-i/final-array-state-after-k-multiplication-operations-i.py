class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # minheap = nums.copy()
        # heapify(minheap)
        for _ in range(k ):
            min_i = 0
            minsofar = nums[0]
            for i, val in enumerate(nums):
                if val < minsofar:
                    min_i = i
                    minsofar = val
            nums[min_i] *= multiplier
            # print(nums)

        return nums