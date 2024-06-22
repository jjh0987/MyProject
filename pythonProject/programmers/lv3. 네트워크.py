def solution(n, network):
    visited = [False for _ in range(n)]
    import collections
    que = collections.deque()
    answer = 0
    for i in range(n):
        if visited[i]:
            continue
        que.append(i)
        while que:
            s = que.popleft()
            visited[s] = True
            for e in range(n):
                if not visited[e] and network[s][e] == 1:
                    que.append(e)
        answer += 1

    return answer