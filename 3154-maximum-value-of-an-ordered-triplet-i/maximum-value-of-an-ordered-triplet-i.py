class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        ans = nums[0] - nums[1]
        ans *= nums[2]
        triplet = [0,1,2]
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1 , N):
                    if (nums[i] - nums[j])*nums[k] > ans:

                        ans = (nums[i] - nums[j])*nums[k]
                        triplet = [i, j, k]

        return max(0,ans)

        