cacheSize = 0
cities = ['la','la']

if cacheSize > 0:
    cities = [i.lower() for i in cities]
    import collections
    cities = collections.deque(cities)
    cache = collections.deque([])
    cache.append(cities.popleft())
    hit = 0
    miss = 1
    while cities:
        tar = cities.popleft()
        if tar in cache:
            hit += 1
            del cache[cache.index(tar)]
            cache.append(tar)
        else:
            miss += 1
            cache.append(tar)
            if len(cache) > cacheSize:
                cache.popleft()
else:
    hit = 0
    miss = len(cities)