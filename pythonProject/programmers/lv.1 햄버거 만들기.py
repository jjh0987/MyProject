ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
stack = []
import collections
ingredient = collections.deque(ingredient)
cnt = 0
while ingredient:
    tar = ingredient.popleft()
    stack.append(tar)
    if stack[-4:] == [1,2,3,1]:
        for _ in range(4):
            stack.pop()
        cnt += 1