class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        cnt = 0
        for ch in s:
            if ch == "[":
                cnt += 1                
            elif cnt > 0:
                cnt -= 1

        # print(stack)
        return (cnt + 1)//2