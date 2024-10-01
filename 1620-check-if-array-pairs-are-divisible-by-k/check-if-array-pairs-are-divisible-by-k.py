class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        umap = {}
        for num in arr:
            rem = num % k
            if (k - rem) % k in umap:
                umap[(k - rem) % k] -= 1
                if umap[(k - rem) % k] <= 0:
                    del umap[(k - rem) % k]
            else:
                if rem not in umap:
                    umap[rem] = 0
                umap[rem] += 1
        # print(umap)
        return True if len(umap) == 0 else False
            
