P = list(map(int,input().split()))
X,Y,R = map(int,input().split())
if X in P:
    print(P.index(X)+1)
else:
    print(0)