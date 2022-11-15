import collections
queue1 = collections.deque([1,1])
queue2 = collections.deque([1,5])
init1 = sum(queue1)
init2 = sum(queue2)
q_length = len(queue1) + len(queue2)
cnt = 0
while 1:
    if init1 > init2:
        try:
            tar = queue1.popleft()
            init1 -= tar
            init2 += tar
            queue2.append(tar)
            cnt += 1
        except:pass
    if init1 < init2:
        try:
            tar = queue2.popleft()
            init1 += tar
            init2 -= tar
            queue1.append(tar)
            cnt += 1
        except:pass
    if init1 == init2:
        break
    if cnt == q_length:
        cnt = -1
        break