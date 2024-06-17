import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int,input().split()))
top = [[top[i],i+1] for i in range(len(top))]

stack = []
ans = [0 for _ in range(len(top)+1)]
while len(top) > 1:
    stack.append(top.pop())
    if stack[-1][0] <= top[-1][0]:
        while stack:
            tp = stack.pop()
            if tp[0] <= top[-1][0]:
                ans[tp[1]] = top[-1][1]
            else:
                stack.append(tp)
                break
print(*ans[1:],sep=' ')