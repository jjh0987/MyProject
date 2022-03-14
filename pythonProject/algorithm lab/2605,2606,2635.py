# 2606
n = int(input())
k = int(input())

computers = [list(map(int,input().split())) for _ in range(k)]

conn = set()
conn.add(1)

while True:
    temp = len(conn)
    for computer in computers:
        if computer[0] in conn:
            conn.add(computer[1])
        elif computer[1] in conn:
            conn.add(computer[0])
    if temp == len(conn):
        break

print(len(conn)-1)



n,m = map(int,input().split())
conn = [list(map(int,input().split())) for _ in range(m)]
conn.sort()
conn_set = [] # add set


# 2605
n = int(input())
number = [int(i) for i in input().split()]
student = []

for num in enumerate(number):
    if num[0] != num[1]:
        temp1 = student[:num[1]]
        temp2 = student[num[1]:]
        temp1 += [1+num[0]]
        student = temp1 + temp2
    else:
        student.append(num[0] + 1)
student.reverse()
student = [str(i) for i in student]
print(' '.join(student))

# 2635
from collections import deque
n = int(input())
check = list(range(n//2+1,n+1))
idx_ls = []
temp_ls = []
for second in check:
    queue = deque()
    queue.append(n)
    queue.append(second)
    temp = 0
    idx = 1
    while temp >= 0:
        temp1 = queue.popleft()
        temp2 = queue.popleft()
        temp = temp1 - temp2
        queue.appendleft(temp)
        queue.appendleft(temp2)
        queue.append(temp1)
        idx += 1
    idx_ls.append(idx)
    temp_ls.append(queue)

ans = temp_ls[idx_ls.index(max(idx_ls))]
temp = ans.popleft()
ans.append(temp)
ans.popleft()

print(max(idx_ls))
ans = [str(i) for i in list(ans)]
print(' '.join(ans))