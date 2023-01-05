s = "[](){}"

import collections
s = collections.deque(s)

def correct(s):
    s = list(s)
    stack = []
    for i in s:
        stack.append(i)
        try:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
            elif stack[-1] == '}' and stack[-2] == '{':
                stack.pop()
                stack.pop()
            elif stack[-1] == ']' and stack[-2] == '[':
                stack.pop()
                stack.pop()
        except:pass
    if stack:
        return 0
    else:
        return 1

cnt = 0
for _ in range(len(s)):
    cnt += correct(s)
    s.append(s.popleft())