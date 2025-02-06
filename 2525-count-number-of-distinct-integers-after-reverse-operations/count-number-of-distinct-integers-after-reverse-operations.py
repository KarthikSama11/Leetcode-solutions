class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sett = set(nums)
        for num in nums:

            strnum = str(num)
            sett.add(int(strnum[::-1]))
        return len(sett)
