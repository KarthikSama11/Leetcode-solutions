class Solution:
    def rob(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 0:
            return 0
        if N == 1:
            return arr[0]
        if N == 2:
            return max(arr[0], arr[1])
        nums = arr[0:N-1]
        bums = arr[1:N]
        ans = 0
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
        # for i in range(len(bums)):
        #     print(i)
        #     a,b = 0, 0
        #     if i >= 3 :
        #         a = bums[i - 3]
        #     if i >= 2 :
        #         b = bums[i - 2]
        #     bums[i] += max(a,b)
        #     ans = max(ans, bums[i])
        
        return ans

        
