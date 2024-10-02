from sortedcontainers import SortedSet
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ss = SortedSet(arr)
        for i, v in enumerate(arr):
            arr[i] = ss.index(v) + 1
        return arr