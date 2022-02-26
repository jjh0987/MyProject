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