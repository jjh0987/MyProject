import sys
input = sys.stdin.readline
n,m = map(int,input().split())
true = set(list(map(int,input().split()))[1:])
graph = {i:[] for i in range(1,m+1)}

for j in range(1,m+1):
    target = list(map(int,input().split()))
    for i in target[1:]:
        graph[j].append(i)

for _ in range(50):
    cnt = int(m)
    for i in range(1,m+1):
        flag = False
        for j in graph[i]:
            if j in true:
                cnt -= 1
                flag = True
                break
        if flag:
            for j in graph[i]:
                true.add(j)
print(cnt)