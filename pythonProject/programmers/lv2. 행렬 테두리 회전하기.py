from collections import deque

def solution(rows, columns, queries):
    answer = []
    mapping = []
    for i in range(rows):
        tp = []
        for j in range(columns):
            tp.append(columns*i+j+1)
        mapping.append(tp)

    def rotation(mapping,lst):
        x1,y1,x2,y2 = lst
        queue = deque()
        for i in range(y1-1,y2-1):
            queue.append(mapping[x1-1][i])
        for i in range(x1-1,x2-1):
            queue.append(mapping[i][y2-1])
        for i in range(y2-1,y1-1,-1):
            queue.append(mapping[x2-1][i])
        for i in range(x2-1,x1-1,-1):
            queue.append(mapping[i][y1-1])

        ans = min(queue)
        queue.appendleft(queue.pop())

        for i in range(y1-1,y2-1):
            mapping[x1-1][i] = queue.popleft()
        for i in range(x1-1,x2-1):
            mapping[i][y2-1] = queue.popleft()
        for i in range(y2-1,y1-1,-1):
            mapping[x2-1][i] = queue.popleft()
        for i in range(x2-1,x1-1,-1):
            mapping[i][y1-1] = queue.popleft()

        return mapping,ans


    for query in queries:
        mapping,ans = rotation(mapping, query)
        answer.append(ans)

    return answer

solution(3,4,[[2, 2, 3, 3]])