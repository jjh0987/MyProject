arr = [4,4,4,3,3]

import collections
arr = collections.deque(arr)
ans = []
while 1:
    try:
        ans.append(arr[0])
        check = arr[0]
        while 1:
            tar = arr.popleft()
            if tar != check:
                arr.appendleft(tar)
                break
    except:
        break
