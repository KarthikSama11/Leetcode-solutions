class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        frnd = times[targetFriend]
        times.sort()
        N = len(times)
        seats = [i for i in range(N)]
        heapify(seats)
        pqend = []
        heapify(pqend)
        for s,e in times:
            while len(pqend) and pqend[0][0] <= s:
                _, chair = heappop(pqend)
                heappush(seats, chair)
            if [s,e] == frnd:
                return heappop(seats)
            seat = heappop(seats)
            heappush(pqend, (e, seat))
        return -1