M,N = map(int,input().split())
A_dot = []
for i in range(M):
    A_dot.append(list(map(int,input().split())))
B_dot = []
for i in range(N):
    B_dot.append(list(map(int,input().split())))

intersection_dot = []
#for b in B_dot:
#    for a in A_dot:
#        if a[0]