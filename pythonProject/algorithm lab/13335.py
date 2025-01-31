import sys
import collections
input = sys.stdin.readline
n,w,L = map(int,input().split())
truck = collections.deque(list(map(int,input().split())))
bridge = collections.deque([0 for _ in range(w)])

t = 0
while truck:
    t += 1
    bridge.popleft()
    tp = truck.popleft()
    if sum(bridge) + tp <= L:
        bridge.append(tp)
    else:
        bridge.append(0)
        truck.appendleft(tp)

print(t+w)