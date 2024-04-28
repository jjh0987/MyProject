import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int,input().split()))
q = int(input())

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    answer[i][i] = 1

for i in range(1,n):
    if seq[i] == seq[i-1]:
        answer[i-1][i] = 1

for j in range(2,n):
    for i in range(j,n):
        if answer[i-j+1][i-1] == 1:
            if seq[i] == seq[i-j]:
                answer[i-j][i] = 1

for _ in range(q):
    s,e = map(int,input().split())
    print(answer[s-1][e-1])