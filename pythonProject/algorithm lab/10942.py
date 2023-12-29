import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int,input().split()))
q = int(input())

def isP(x):
    for i in range((len(x)//2)+1):
        if x[i] != x[-i-1]:
            return 0
    if not x:
        return 0
    return 1

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    answer[i][i] = 1
for i in range(n-1):
    if seq[i] == seq[i+1]:
        answer[i][i+1] = 1
# for k in range(2,n+1):
#     for i in range(k):
#         for j in range(i+2,k):
#             if seq[i] != seq[j]:
#                 continue
#             if answer[i+1][j-1] == 1:
#                 answer[i][j] = 1

for _ in range(q):
    s,e = map(int,input().split())
    # print(answer[s-1][e-1])
    print(isP(seq[s-1:e]))
