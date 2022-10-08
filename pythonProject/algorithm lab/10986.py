import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = list(map(int,input().split()))
S = [0 for _ in range(n)]
S[0] = A[0]
for i in range(1,n):
    S[i] += S[i-1] + A[i]

S = [i%m for i in S]

import collections
S = collections.Counter(S)
ans = S[0]
def combi_count(i):
    return int((S[i]*(S[i]-1))/2)

for i in S.keys():
    ans += combi_count(i)

print(ans)