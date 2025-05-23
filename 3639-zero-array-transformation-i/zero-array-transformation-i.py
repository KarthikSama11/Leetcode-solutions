class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #classic linesweep problem
        N = len(nums)
        line = [0]*(N+1)
        for l,r in queries:
            line[l] += 1

            line[r + 1] += -1
        print(nums)
        print(line)
        prefix = 0
        for i in range(N):
            prefix += line[i]
            if nums[i] > 0 and prefix < nums[i]:
                return False
        return True