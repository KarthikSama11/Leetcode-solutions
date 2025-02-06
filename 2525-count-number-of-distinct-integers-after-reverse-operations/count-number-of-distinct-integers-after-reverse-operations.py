class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        sett = set()
        for num in nums:
            sett.add(num)
            strnum = str(num)
            sett.add(int(strnum[::-1]))
        return len(sett)
