works = [1,1]
n = 3

if sum(works) > n:
    import collections
    works = collections.Counter(works)
    while n > 0:
        key = max(works)
        while works[key] > 0:
            if n == 0:
                break
            works[key] -= 1
            n -= 1
            works[key-1] += 1
        if works[key] == 0:
            del works[key]

    ans = 0
    for key in works:
        for _ in range(works[key]):
            ans += key**2
else:ans=0

