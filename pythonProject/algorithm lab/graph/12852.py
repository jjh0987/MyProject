k = int(input())
ans = []
def sol(x):
    if x == 1:
        ans.append(x)
    elif x%3 == 0:
        ans.append(x)
        sol(x//3)
    elif x%2 == 0:
        ans.append(x)
        sol(x//2)
    else:
        ans.append(x)
        sol(x-1)

sol(k)
import collections
dp = collections.deque([[k,k,k],[0,0,0]])

DP = dp.popleft()

a = DP[0]