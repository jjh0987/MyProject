import sys
input = sys.stdin.readline
n = int(input())

tp = [[int(input()),i] for i in range(n)]
tp_tp = sorted(tp)

ans = 0
for i in range(n):
    if tp_tp[i][1] - tp[i][1] > ans:
        ans = tp_tp[i][1] - tp[i][1]

print(ans+1)