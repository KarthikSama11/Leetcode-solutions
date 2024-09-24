class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashset = set()
        for num in arr1:
            hashset.add(num)
            while num:
                num //=10
                hashset.add(num)
        ans = 0
        for num in arr2:
            while num :
                # print(num)
                if num in hashset:
                    ans = max(ans, len(str(num)))
                num //= 10
        return ans
