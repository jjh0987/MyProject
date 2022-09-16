import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = list(map(int,input().split()))
S = [0]*(n+1)

for i in range(n):
    S[i+1] = S[i] + A[i]

for i in range(m):
    span = list(map(int,input().split()))
    print(S[span[1]]-S[span[0]-1])



n = int(input())
S = [0]*(n+1)
