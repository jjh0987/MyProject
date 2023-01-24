k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

import collections
tangerine = collections.Counter(tangerine)
target = []
for i in tangerine:
    target.append([i,tangerine[i]])

target.sort(key=lambda x:x[1])
check = 0
ans = 0
while 1:
    tar = target.pop()
    check += tar[1]
    if check >= k:
        ans += 1
        break
    ans += 1