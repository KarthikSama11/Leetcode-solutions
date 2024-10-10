class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i, num in enumerate(nums):
            if len(stack) == 0:
                stack.append(i)
            else:
                if nums[stack[-1]] > num:
                    stack.append(i)
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()
        return ans