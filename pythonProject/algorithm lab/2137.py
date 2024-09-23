n, m = map(int, input().split())

mini = []
tar = 1
for i in range(2, 32768):
    for j in range(int(max(1, n / m * i - 1)), int(min(32768, n / m * i + 1)) + 1):
        tar = abs(n / m - j / i)
        if tar != 0:
            mini.append((tar, i, j))

mini.sort()
print(mini[0][2], mini[0][1])