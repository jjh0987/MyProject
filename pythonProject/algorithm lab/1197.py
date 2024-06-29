import sys
input = sys.stdin.readline
v,n = map(int,input().split())

graph = {i:[] for i in range(1,v+1)}
for _ in range(n):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

for i in range(1,v+1):
    graph[i].sort()

answer = []
for s in range(1,v+1):
    ans = 0
    visited = [False for _ in range(v+1)]
    visited[s] = True
    cnt = 1
    while cnt < v:
        for w,e in graph[s]:
            if visited[e]:
                continue
            visited[e] = True
            ans += w
            s = int(e)
            break
        cnt += 1
        print(ans,s)
    print('cut')
    if sum(visited) == v:
        answer.append(ans)
print(min(answer))