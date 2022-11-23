numbers = [1, 1, 1, 1, 1]
target = 3
cnt = 0
def dfs(x):
    global cnt
    if x == target:
        cnt += 1
    else:
        dfs(x)