import sys
input = sys.stdin.readline
n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

ans = [0 for _ in range(n)]
try:
    ans[0] = seq[0]
    ans[1] = seq[0]+seq[1]
    ans[2] = max(seq[0]+seq[2],seq[1]+seq[2])
    for i in range(3,n):
        ans[i] = max(ans[i-2]+seq[i],ans[i-3]+seq[i-1]+seq[i])
except:pass
print(ans[-1])