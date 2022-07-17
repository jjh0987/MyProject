# 17219
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

pw_dict = dict()
for _ in range(n):
    address,pw = input().split()
    pw_dict[address] = pw

for _ in range(m):
    print(pw_dict[input().rstrip('\n')])

# 9375
cnt = 0
iteration = int(input())
from collections import deque
while cnt != iteration:
    ans = 0
    n = int(input())

    tp = [input().split()[1] for _ in range(n)]
    tp_set = list(set(tp))
    cloth_dict = {i:0 for i in tp_set}
    for i in tp:
        cloth_dict[i] += 1

    queue = deque(list(cloth_dict.values()))
    conf = queue.copy()
    for i in range(1,len(cloth_dict)+1):
        while 1:
            pre_ans = 1
            for _ in range(i):
                num = queue.pop()
                pre_ans *= num
                queue.appendleft(num)
            ans += pre_ans
            if queue == conf:
                break

    cnt += 1
    print(ans)

# 9375
cnt = 0
iteration = int(input())
while cnt != iteration:
    ans = 1
    n = int(input())

    tp = [input().split()[1] for _ in range(n)]
    tp_set = list(set(tp))
    cloth_dict = {i:0 for i in tp_set}
    for i in tp:
        cloth_dict[i] += 1

    tp_list = [i+1 for i in list(cloth_dict.values())] # 입지 않는경우에대해 +1
    for i in tp_list:
        ans *= i
    print(ans-1)
    cnt += 1

