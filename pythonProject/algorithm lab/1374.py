import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
heapq.heapify(h)
for _ in range(n):
    heapq.heappush(h, list(map(int,input().split()))[1:])

rev_h = []
heapq.heapify(rev_h)
while h:
    if not rev_h:
        s,e = heapq.heappop(h)
        heapq.heappush(rev_h, [e,s])
    else:
        mini = heapq.heappop(rev_h)
        tar = heapq.heappop(h)
        if mini[0] <= tar[0]:
            heapq.heappush(rev_h, [tar[1],mini[1]])
        else:
            heapq.heappush(rev_h, [tar[1],tar[0]])
            heapq.heappush(rev_h, mini)
print(len(rev_h))                        