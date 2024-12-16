class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for i,v in enumerate(nums)]
        heapify(heap)
        for _ in range(k ):
            _, i = heappop(heap)
            nums[i] *= multiplier
            heappush(heap, (nums[i], i))
            # print(nums)

        return nums