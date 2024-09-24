class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        umap = defaultdict(int)
        count, ans = 0, 0
        for i, j in intervals:
            umap[i] += 1
            umap[j] -= 1
        for k, v in sorted(umap.items()):
            count += v
            ans = max(ans, count)
        return ans