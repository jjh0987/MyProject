# 1
paper = [1,0,0,3,0,1]
paper = [7,5,8,10,6,9,5]
paper = [3,0,3,0,3,0]

import collections
paper.sort(reverse=True)
paper = collections.deque(paper)

tp = []
marking = [0]*len(paper)
for i in range(len(paper)):
    tp.append(paper.popleft())
    if len(tp)**2 <= sum(tp):
        marking[i] += i+1

marking
# 2
num = 5
mark = [1,2,3,1] # 1,2,3,4 num

cnt = 1
start = mark[0]
while cnt != num:
    start = mark[start]
    cnt += 1

print(start)

# 3
arr = [1,2,3,4,5,6]


for i in range(20):
    if len(arr) > 2**i:
        n = 2**(i+1)

import collections
arr.reverse()

bundle = collections.deque([arr])
i = 0
while i < n-1:
    target = bundle.popleft()
    if len(target)%2 == 0:
        tp1 = target[:len(target) // 2]
        tp1.reverse()
        if tp1:
            bundle.append(tp1)
        tp2 = target[len(target) // 2:]
        tp2.reverse()
        if tp2:
            bundle.append(tp2)
    elif len(target)%2 == 1:
        tp1 = target[:len(target)//2+1]
        tp1.reverse()
        if tp1:
            bundle.append(tp1)
        tp2 = target[len(target)//2+1:]
        tp2.reverse()
        if tp2:
            bundle.append(tp2)
    i += 1

ans = []
for i in bundle:
    ans.append(i[0])