class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "[":
                stack.append(ch)
                
            else:
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(ch)
        # print(stack)
        return ((len(stack)//2)+1)//2