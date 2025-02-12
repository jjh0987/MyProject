import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l,n = map(int,input().split())
    ants = [int(input()) for _ in range(n)]
    ants.sort()
    m,M = 0,0
    for i in ants:
        m = max(m,min(i,l-i))
        M = max(M,max(i,l-i))
    print(m,M)          