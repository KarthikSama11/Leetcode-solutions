class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans = 0
        umap = defaultdict(int)
        MOD = 10**9 + 7
        def rev(num):
            r = 0
            while num:
                r = r * 10 + num % 10
                num //= 10
            return r
            s_num = str(num)
            s_num = s_num[::-1]
            num = int(s_num)
            return num
        for num in nums:
            minus = num - rev(num)
            ans = (ans + umap[minus] % MOD) % MOD
            umap[minus] += 1
        return ans 
