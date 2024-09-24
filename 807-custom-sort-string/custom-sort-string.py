class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def customSort(c1, c2):
            i1, i2 = 26, 26
            # print(c1, c2)
            for i, ch in enumerate(order):
                if c1 == ch:
                    i1 = i
                if c2 == ch:
                    i2 = i
            
            return i1 - i2
        ans = sorted(s, key = cmp_to_key(customSort))
        # print(arr)
        return "".join(ans)