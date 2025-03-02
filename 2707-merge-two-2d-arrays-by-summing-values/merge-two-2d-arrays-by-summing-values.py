class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        umap = {}
        for id, val in nums1:
            umap[id] = val
        for id, val in nums2:
            if id in umap:
                umap[id] += val
            else:
                umap[id] = val
        
        return sorted(list(umap.items()))