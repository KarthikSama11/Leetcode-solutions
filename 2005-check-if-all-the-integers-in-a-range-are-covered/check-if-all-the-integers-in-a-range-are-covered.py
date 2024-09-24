class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sweep = defaultdict(int)
        for l, r in ranges:
            sweep[l] += 1
            sweep[r + 1] -= 1
        count = 0
        # print(sorted(sweep.items()))
        for i in range(1, right + 1):
            # if sweep[i] >= 0:
            count += sweep[i]
            # print(i, count)
            if left <= i <= right and count <= 0:
                return False
            # if sweep[i] < 0:
            #     count += sweep[i]
        return True
