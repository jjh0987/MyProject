import sys
import math

input = sys.stdin.readline
n = int(input())
tar = [list(map(float,input().split())) for _ in range(n)]

def find(s):
    visited = [False for _ in range(n)]
    dist_map = []
    for i in tar:
        tp = []
        for j in tar:
            tp.append(math.dist(i,j))
        dist_map.append(tp)

    answer = 0
    for _ in range(n-1):
        visited[s] = True
        target = float('inf')
        for j in range(n):
            if visited[j] == False: #  and dist_map[s][j] > 0:
                target = min(target,dist_map[s][j])
        answer += target
        s = dist_map[s].index(target)
    return answer

print(round(min([find(i) for i in range(n)]),2))



import sys
import math

input = sys.stdin.readline
n = int(input())
tar = [list(map(float, input().split())) for _ in range(n)]

def find(s):
    visited = [False for _ in range(n)]
    dist_map = []
    for i in tar:
        tp = []
        for j in tar:
            tp.append(math.dist(i, j))
        dist_map.append(tp)

    answer = 0
    visited[s] = True

    for _ in range(n - 1):
        target = float('inf')
        next_vertex = -1  # 다음 정점 초기화

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and dist_map[i][j] > 0 and dist_map[i][j] < target:
                        target = dist_map[i][j]
                        next_vertex = j  # 다음 정점 설정

        if next_vertex != -1:
            visited[next_vertex] = True
            answer += target

    return answer

result = min([find(i) for i in range(n)])
print(round(result, 2))