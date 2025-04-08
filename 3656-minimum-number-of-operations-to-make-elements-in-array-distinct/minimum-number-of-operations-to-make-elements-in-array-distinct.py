class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashmap = {}
        N = len(nums)
        ops = 0
        repeat = -1
        for i in range(N):
            if nums[i] in hashmap:
                repeat = max(repeat, hashmap[nums[i]])
            hashmap[nums[i]] = i
            
        # print((repeat+1)//3)
        return (repeat)//3 +1

