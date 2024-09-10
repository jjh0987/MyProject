import sys
input = sys.stdin.readline
import heapq
max_h = []
min_h = []
heapq.heapify(max_h)
heapq.heapify(min_h)

n = int(input())
problem = set()
for _ in range(n):
    n,v = map(int,input().split())
    heapq.heappush(max_h,(-v,-n))
    heapq.heappush(min_h,(v,n))
    problem.add(n)

solved = set()
m = int(input())
for _ in range(m):
    q = input().split()
    if q[0] == 'solved':
        solved.add(int(q[1]))
        try:
            problem.remove(int(q[1]))
        except:pass
        while 1:
            tp = heapq.heappop(max_h)
            if -tp[1] not in solved:
                break
        heapq.heappush(max_h, tp)
        while 1:
            tp = heapq.heappop(min_h)
            if tp[1] not in solved:
                break
        heapq.heappush(min_h, tp)
    elif q[0] == 'recommend':
        if q[1] == '1':
            tp = heapq.heappop(max_h)
            print(-tp[1])
            heapq.heappush(max_h, tp)
        else:
            tp = heapq.heappop(min_h)
            print(tp[1])
            heapq.heappush(min_h,tp)
    else:
        q[1],q[2] = int(q[1]),int(q[2])
        problem.add(q[1])
        try:
            solved.remove(q[1])
        except:pass
        heapq.heappush(min_h,(q[2],q[1]))
        heapq.heappush(max_h,(-q[2],-q[1]))


