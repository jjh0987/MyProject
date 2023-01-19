n = 3
network = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
network = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
ans = []
for i in range(n):
    tp = set()
    for j in range(n):
        if network[i][j] == 1:
            if i == j:
                continue
            if network[j][i] == 1:
                tp.add(j)
                tp.add(i)
    ans.append(list(tp))

ans = {i:ans[i] for i in range(n)}
answer = []
mapping = [0]*n
for i in ans:
    mapping[i] = 1
    tp = set()
    for j in ans[i]:
        tp.add(j)
    answer.append(tp)


    if mapping[j] == 1:
        continue
    if i in ans[j]:
        mapping[j] = 1
        answer += 1
