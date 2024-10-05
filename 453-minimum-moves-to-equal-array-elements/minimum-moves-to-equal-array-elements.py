class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """

        1 2 3 4
        4 5 6 4
        6 7 6 6
        7 7 7 7 

        1 2 3 4 5
        4 6 7 8 5
        8 10 11 8 9
        11 13 11 11 12
        13 13 13 13 14
        14 14 14 14 14
        """
        nums.sort()
        ans = 0
        start = nums[0]
        for num in nums:
            ans += num - start
        return ans
