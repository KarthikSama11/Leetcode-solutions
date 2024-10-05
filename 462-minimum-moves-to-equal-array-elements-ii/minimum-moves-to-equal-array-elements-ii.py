class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """
        1 2 3 4 14 6 
        7 2 3 4 14 5 
        7 7 3 4 14 4 
        7 7 7 4 14 3 
        7 7 7 7 14 7
        7 7 7 7 7
        1 2 9 10
        """
        # total = sum(nums)
        nums.sort()
        N = len(nums)
        median = N // 2
        avg = nums[median]
        ans = 0
        # print(avg)
        for num in nums:
            # print(avg - num)
            ans += abs(avg - num)
        return ans