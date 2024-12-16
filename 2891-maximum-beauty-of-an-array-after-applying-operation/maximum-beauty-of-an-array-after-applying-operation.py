class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        arr = []
        umap = {}
        for num in nums:
            arr.append((num - k, num + k + 1))
            l,r = arr[-1]
            if l not in umap:
                umap[l] = 0
            if r not in umap:
                umap[r] = 0
            umap[l] += 1
            umap[r] -= 1
        ans = 1
        cur = 0
        for k, v in sorted(umap.items()):
            cur += v
            ans = max(ans, cur)
        return ans