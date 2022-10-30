n = int(input())
tar = bin(n)[2:]

import collections
q = collections.deque(tar)
gap = []
while q:
    if q.popleft() == '1':
        cnt = 0
        while 1:
            try:
                test = q.popleft()
                if test == '0':
                    cnt += 1
                else:break
            except:break
        if test == '1':
            gap.append(cnt)
        else:
            pass
print(max(gap))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(N):
    tar = bin(N)[2:]
    q = collections.deque(tar)
    gap = []
    while q:
        if q.popleft() == '1':
            cnt = 0
            while 1:
                try:
                    test = q.popleft()
                    if test == '0':
                        cnt += 1
                    else:
                        break
                except:
                    break
            if test == '1':
                gap.append(cnt)
            else:
                pass
    return max(gap)
solution(32)