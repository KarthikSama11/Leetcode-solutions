class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
      # skipinds = [1e6]*len(s)
      # count = 0
      # for i, ch in enumerate(s):
      #   if ch ==  '(':
      #     count += 1
      #   elif ch == ')':
      #     count -= 1
      #   else:
      #     continue
      #   skipinds[i] = count
      # r = len(skipinds) - 1
      # while r >= 0:
      #   if skipinds[r] == 0:
      #     break
      #   r -= 1
      # ans = ""
      # for i in range(len(skipinds)):
      #   if 
      stack = []
      # ignore = set()
      for i, ch in enumerate(s):
        if ch == '(':
          stack.append((i, ch))
        elif ch == ')':
          if len(stack) and stack[-1][1] == '(':
            stack.pop()
          else:
            stack.append((i,ch))

      stack = set(stack)
      
      ans = ""
      for i, ch in enumerate(s):
        if (i, ch) in stack:
          continue
        ans += ch
      return ans



