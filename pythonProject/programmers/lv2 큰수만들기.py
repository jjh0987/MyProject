number = '1237252841'
k = 5

import collections
number = collections.deque([int(i) for i in number])

stack = []
while k > 0:
    tar = number.popleft()
    stack.append(tar)
    while stack[-1] > number[0]:
        if k == 0:
            break
        stack.append(number.popleft())
        k -= 1
    else:
        if stack[-1] == number[0]:
            stack.append(number.popleft())
        else:
            stack.pop()
            k -= 1