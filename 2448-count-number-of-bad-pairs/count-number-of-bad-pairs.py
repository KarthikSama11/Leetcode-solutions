class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        totalpairs = (N * (N - 1))//2
        good = 0
        umap = defaultdict(int)
        for i, num in enumerate(nums):
            d = num - i
            good += umap[d]
            umap[d] += 1
        return totalpairs - good
            