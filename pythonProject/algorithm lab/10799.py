import sys
input = sys.stdin.readline
data = input().rstrip('\n')

import collections
# data = collections.deque(list('(((()(()()))(())()))(()())'))
data = collections.deque(data)
stack = []
answer = 0

while data:
    try:
        a = data.popleft()
        b = data.popleft()
        if a == '(' and b == ')':
            answer += len(stack)
        elif a == '(' and b == '(':
            stack.append(a)
            data.appendleft(b)
        else:
            answer += 1
            stack.pop()
            data.appendleft(b)
    except:
        break
print(answer+len(stack))