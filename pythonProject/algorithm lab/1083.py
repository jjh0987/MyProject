import sys
input = sys.stdin.readline
n = int(input())
local = list(map(int,input().split()))
s = int(input())

answer_up = []
answer_down = []
cnt = 0
while s > 0:
    max_idx = local.index(max(local))
    if s >= max_idx:
        answer_up.append(max(local))
        s -= max_idx
        local.pop(max_idx)
        cnt += 1
    else:
        min_idx = local.index(min(local))
        if min_idx == len(local)-1:
            answer_down.append(local.pop())
            continue
        local[min_idx], local[min_idx+1] = local[min_idx+1], local[min_idx]
        s -= 1

answer_up.extend(local)
answer_up.extend(sorted(answer_down,reverse=True))
print(*answer_up)