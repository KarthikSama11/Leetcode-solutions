from functools import cmp_to_key
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        def compare(a, b):
            if a[0] < b[0]:
                return -1
            if a[0] > b[0]:
                return 1
            if a[0] == b[0]:
                if a[1] <= b[1]:
                    return -1
                if a[1] > b[1]:
                    return 1
        events.sort(key = cmp_to_key(compare))
        # events.sort(key = lambda x: x[0])
        print(events)
        l, N, ans = 0, len(events), 0
        pq = []
        heapify(pq)
        startat, endat = events[0][0], 0
        for s,e in events:
            endat = max(endat, e)
        # intervals = defaultdict(list)
        # for s,e in events:
        #     intervals[s] = e
        for time in range(startat, endat + 1):
            while l < N and events[l][0] <= time:
                heappush(pq, events[l][1])
                l += 1
                # print(time, pq)
            while len(pq) and pq[0] < time:
                heappop(pq)
            if len(pq):
                # print(time, pq[0])
                heappop(pq)
                ans += 1
            
        return ans
            
        
        

        