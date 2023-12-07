import sys
input = sys.stdin.readline
n = int(input())
h = list(map(int,input().split()))

ans = len(h)*2 + h[0] + h[-1] + 2*sum(h)
for i in range(1,len(h)):
    ans += abs(h[i]-h[i-1])

print(ans)