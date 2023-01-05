scoville = [1, 2]
K = 7

from heapq import heappop,heappush

heap = []
for i in scoville:
    heappush(heap,i)

ans = 0
check = 0
flag = 0
while 1:
    try:
        tar = heappop(heap)
        if tar < K:
            check = tar + heappop(heap)*2
            heappush(heap,check)
            ans += 1
        else:
            break
    except:
        flag = 1
        break