class Solution:
    def rob(self, bums: List[int]) -> int:
        N = len(bums)
        if N == 0:
            return 0
        if N == 1:
            return bums[0]
        if N == 2:
            return max(bums[0], bums[1])
        nums = bums[0:N-1]
        arr = bums[1:N]
        ans = 0
        
        for i in range(0, len(nums)):
            print(i)
            a,b = 0, 0
            if i - 3 >= 0:
                a = nums[i - 3]
            if i - 2 >= 0:
                b = nums[i - 2]
            nums[i] += max(a,b)
            ans = max(ans, nums[i])
        
        print("-------")
        for i in range(1, len(arr)):
            print(i)
            a,b = 0, 0
            if i >= 3 :
                a = arr[i - 3]
            if i >= 2 :
                b = arr[i - 2]
            arr[i] += max(a,b)
            ans = max(ans, arr[i])
        
        return ans

        
