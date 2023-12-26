import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
heapq.heapify(h)
for _ in range(n):
    heapq.heappush(h, int(input()))

ans = 0
if len(h) >= 2:
    while len(h) > 1:
        try:
            a = heapq.heappop(h)
            b = heapq.heappop(h)
            if a <= 0 and b <= 0:
                ans += a * b
            elif a <= 0 and b > 0:
                ans += a + b
            elif a == 1 and b == 1:
                ans += a + b
            else:
                heapq.heappush(h, a)
                heapq.heappush(h, b)
                break
        except:
            heapq.heappush(h, a)
            break

h.sort()
while h:
    try:
        a = h.pop()
        b = h.pop()
    except:
        ans += a
        break
    ans += a * b

print(ans)