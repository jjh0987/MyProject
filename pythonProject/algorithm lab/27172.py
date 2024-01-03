import sys
input = sys.stdin.readline
n = int(input())
target = list(map(int,input().split()))
visited = [False for _ in range(1000001)]
for i in target:
    visited[i] = True
answer = [0 for _ in range(1000001)]

for i in range(len(target)):
    net = target[i]
    for j in range(2*net,1000001,net):
        if visited[j]:
            answer[j] -= 1
            answer[net] += 1

for i in target:
    print(answer[i],end=' ')