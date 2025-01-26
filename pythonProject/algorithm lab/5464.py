import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parking_fee = [int(input().rstrip('\n')) for _ in range(n)]
car_weight = [int(input().rstrip('\n')) for _ in range(m)]

import collections
input_que = collections.deque()
out_que = collections.deque()
visited = {i:0 for i in range(n)}
cnt = 0
answer = 0

for _ in range(2*m):
    tp = int(input())
    if tp > 0:
        input_que.append(tp)
    else:
        tp = -tp
        out_que.append(tp)

    while input_que:
        if cnt == n:
            break
        tp = input_que.popleft()
        for i in visited:
            if not visited[i]:
                visited[i] = tp
                cnt += 1
                answer += car_weight[tp-1]*parking_fee[i]
                break
    try:
        tp = out_que.popleft()
        for i in visited:
            if visited[i] == tp:
                visited[i] = 0
                cnt -= 1
                break
    except:pass
print(answer)