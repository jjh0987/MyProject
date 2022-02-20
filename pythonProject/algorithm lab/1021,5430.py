# 1021
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

target = list(map(int,input().split()))

queue = deque()
for i in range(1,n+1):
    queue.append(i)

cnt = 0
for i in target:
    cnt_l = 0
    copy_q1 = queue.copy()
    while copy_q1[0] != i:
        copy_q1.append(copy_q1.popleft())
        cnt_l += 1

    cnt_r = 0
    copy_q2 = queue.copy()
    while copy_q2[0] != i:
        copy_q2.appendleft(copy_q2.pop())
        cnt_r += 1

    cnt += min(cnt_r,cnt_l)
    if cnt_r > cnt_l:
        queue = copy_q1
    else:
        queue = copy_q2
    queue.popleft()

print(cnt)

# 5430
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
for i in range(n):
    try:
        operation = input().rstrip('\n')

        k = int(input())

        queue = deque()

        list_input = input()
        try:
            for j in list_input[1:len(list_input)-2].split(','):
                queue.append(int(j))
        except:
            pass

        if k != len(queue):
            print('error')
            continue

        R_cnt = 0
        for i in operation:
            if R_cnt % 2 == 0:
                if i == 'D':
                    queue.popleft()
                else:
                    R_cnt += 1
            else:
                if i == 'D':
                    queue.pop()
                else:
                    R_cnt += 1

        if R_cnt % 2 == 0:
            print('['+",".join(map(str,list(queue)))+']')
        else:
            queue.reverse()
            print('['+",".join(map(str,list(queue)))+']')
    except:
        print('error')