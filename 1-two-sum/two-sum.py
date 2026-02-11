
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        umap = defaultdict(int)
        for idx, val in enumerate(nums):
            if target - val in umap:
                return [idx, umap[target-val]]
            umap[val] = idx
        