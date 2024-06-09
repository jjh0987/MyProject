import sys
input = sys.stdin.readline

# n = int(input())
import collections
# buildings = collections.deque([list(map(int,input().split())) for _ in range(n)])

n = 8
data = '''1 11 5
2 6 7
3 13 9
12 7 16
14 3 25
19 18 22
23 13 29
24 4 28'''
buildings = collections.deque([list(map(int,i.split())) for i in data.split('\n')])
stack = [buildings.popleft()]
while buildings:
    l,v,r = buildings.popleft()
    if stack[-1][0] <= r <= stack[-1][2]:
        if v <= stack[-1][1]:
            stack[-1][1] = v
    elif l <= stack[-1][0] < r:
        stack.pop()
        stack[-1][2] = l
        stack.append([l,v,r])
    elif stack[-1][0] <= l <= stack[-1][2]:
        stack.append([l,max(v,stack[-1][1]),stack[-1][2]])
        stack[-2][2] = l
        stack.append([stack[-1][2],v,r])
    elif l <= stack[-1][0]:
        l = stack[-1][2]
        stack.append([l,v,r])
    else:
        stack.append([l,v,r])

    print(*stack,sep='\n')
    print(buildings)