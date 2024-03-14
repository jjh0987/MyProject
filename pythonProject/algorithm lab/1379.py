
import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
heapq.heapify(h)
for _ in range(n):
    r,s,e = list(map(int,input().split()))
    heapq.heappush(h, [s,e,r])

rev_h = []
heapq.heapify(rev_h)
graph = []
while h:
    if not rev_h:
        s,e,r = heapq.heappop(h)
        heapq.heappush(rev_h, [e,s,r])
    else:
        mini = heapq.heappop(rev_h)
        tar = heapq.heappop(h)
        if mini[0] <= tar[0]:
            heapq.heappush(rev_h, [tar[1],mini[1],mini[2]])
        else:
            heapq.heappush(rev_h, [tar[1],tar[0],tar[2]])
            heapq.heappush(rev_h, mini)
