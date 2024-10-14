# import math
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = []
        heapify(pq)
        for i,num in enumerate(nums):
            heappush(pq, -num)
            # print(pq)
            # if len(pq) > k:
            #     heappop(pq)
        ans = 0
        # print(pq)
        for i in range(k):
            val = heappop(pq)
            val *= -1
            ans += val
            # nums[idx] = math.ceil((val)/3)
            heappush(pq,-math.ceil(val/3))
        return ans

 