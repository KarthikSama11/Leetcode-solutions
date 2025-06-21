class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates = []
        prefix = 0
        candles = []
        N = len(plates)
        res = []
        for i, c in enumerate(s):
            if c == "|":
                plates.append(i)
            prefix += 1 if len(plates) and c == "*" else 0
            candles.append(prefix)
        def bs():
            pass
        print(plates, candles)
        for query in queries:
            start, end = query
            if not len(plates) or start > plates[-1] or end < plates[0]:
                res.append(0)
                continue
            left = N
            l,r =0, len(plates) - 1
            #searching for the first index that is greater than or equal to start
            while l <= r:
                mid = (l + r)//2
                # print("greater than or equal to start")
                # print(l,r, mid, plates[mid])
                if plates[mid] == start:
                    left = plates[mid]
                    break
                elif plates[mid] < start:
                    l = mid + 1
                else:
                    left = plates[mid]
                    r = mid - 1
            right = -1
            l, r = 0, len(plates) - 1
            while l <= r:
                mid = (l + r) // 2
                # print(l,r,mid, plates[mid])
                if plates[mid] == end:
                    right = plates[mid]
                    break
                elif plates[mid] < end:
                    right = plates[mid]
                    l = mid + 1
                else:
                    r = mid - 1
            # print(left, right)
            total = candles[right] - candles[left]
            res.append(total if total > 0 else 0)
        return res

