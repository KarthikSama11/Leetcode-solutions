class Solution:
    def rob(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 0:
            return 0
        if N <= 3:
            return max(arr)
            
        def helper(nums):
            ans = 0
            for i in range(len(nums)):
                print(i)
                a,b = 0, 0
                if i - 3 >= 0:
                    a = nums[i - 3]
                if i - 2 >= 0:
                    b = nums[i - 2]
                nums[i] += max(a,b)
                ans = max(ans, nums[i])
            return ans
        return max(helper(arr[1:N]), helper(arr[0: N - 1]))
        
