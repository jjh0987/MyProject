operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]


import heapq
min_heap = []
max_heap = []

for i in range(len(operations)):
    tar = operations[i].split()
    try:
        if tar[0] == 'I':
            heapq.heappush(min_heap,int(tar[1]))
        elif tar[0] == 'D' and tar[1] == '-1':
            print(heapq.heappop(min_heap))
        elif tar[0] == 'D' and tar[1] == '1':
            while min_heap:
                heapq.heappush(max_heap,-heapq.heappop(min_heap))
            print(-heapq.heappop(max_heap))
            while max_heap:
                heapq.heappush(min_heap,-heapq.heappop(max_heap))
    except:pass

