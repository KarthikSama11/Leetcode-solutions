class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part):
                flag = True
                j = len(stack) - 1
                k = len(part) - 1
                while k >= 0:
                    if stack[j] != part[k]:
                        break
                    j -= 1
                    k -= 1
                if k < 0:
                    stack = stack[0: len(stack) - len(part)]
                    # print(stack)
        return "".join(stack)