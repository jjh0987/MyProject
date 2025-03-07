import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
connections = []
nodes = []
for _ in range(m):
    query = list(map(int,input().split()))
    cnt = 1
    connections.append([query[i]-1 for i in range(cnt,query[0]+cnt)])
    cnt += query[0]
    nodes.append(query[cnt:])

b = list(map(int,input().split()))
for _ in range(q):
    ans = []
    A = list(map(int,input().split()))
    for i in range(m):
        tmep_c = connections[i]
        ans.append(sum([A[tmep_c[j]]*nodes[i][j] for j in range(len(tmep_c))])+nodes[i][-1])
    answer = b[-1]
    for i in range(len(ans)):
        answer += ans[i]*b[i]
    print(answer)