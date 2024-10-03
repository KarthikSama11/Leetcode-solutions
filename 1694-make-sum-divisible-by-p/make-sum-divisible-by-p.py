class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        reqrem = sum(nums) % p
        if reqrem == 0:
            return 0
        prefixsum = 0
        divs = {0: -1}
        ans = len(nums) + 1
        for i, val in enumerate(nums):
            prefixsum += val
            currem = prefixsum % p
            tar = (currem - reqrem + p) % p
            # if tar == currem:
            #     return 1
            # print(i, tar)
            if tar in divs:
                print(tar, currem, i, prefixsum, ans)
                ans = min(ans, i - divs[tar])
            divs[currem] = i
        print(divs)
        return ans if ans < len(nums) else -1