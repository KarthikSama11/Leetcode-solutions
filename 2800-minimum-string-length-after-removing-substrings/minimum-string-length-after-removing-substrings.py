class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i, ch in enumerate(s):
            stack.append(ch)
            while len(stack) >= 2 :
                if stack[-2] + stack[-1] == "AB" or stack[-2] + stack[-1] == "CD":
                    stack.pop()
                    stack.pop()
                else:
                    break
        
        return len(stack)