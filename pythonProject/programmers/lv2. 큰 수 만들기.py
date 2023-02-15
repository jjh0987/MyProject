number = '1924'
k = 2

number = "1231234"
k = 3

number = "4177252841"
k = 4

import collections
number = collections.deque([int(i) for i in list(number)])
stack = []
while k > 0:
    stack.append(number.popleft())
