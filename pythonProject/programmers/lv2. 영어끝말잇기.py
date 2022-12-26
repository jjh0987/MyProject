n = 2
words = ['ac','ca','ac','ac']


import collections

words = collections.deque(words)
check = collections.deque()
check.append(words.popleft())

bag = set()
cnt = 0
flag = 0
while check:
    try:
        check.append(words.popleft())
    except:pass
    pt = len(bag)
    cnt += 1
    if len(check) == 2:
        if check[0][-1] != check[1][0]:
            cnt += 1
            flag = 1
            break
        for s in check:
            if s in bag:
                cnt += 1
                flag = 1
        if flag == 1:
            break
    bag.add(check.popleft())
    if pt == len(bag):
        flag = 1
        break

q,r = divmod(cnt,n)
if r > 0:
    q += 1
elif r == 0:
    r = n


print([r,q])