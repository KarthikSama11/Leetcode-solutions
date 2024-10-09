class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # umap = defaultdict(int)
        # count, ans = 0, 0
        # for i, j in intervals:
        #     umap[i] += 1
        #     umap[j + 1] -= 1
        # for k, v in sorted(umap.items()):
        #     count += v
        #     ans = max(ans, count)
        # return ans
        pq = []
        heapify(pq)
        intervals.sort()
        ans = 0
        for start, end in intervals:
            while len(pq) > 0 and pq[0] <= start:
                heappop(pq)
            heappush(pq, end)
            ans = max(ans, len(pq))
        return ans