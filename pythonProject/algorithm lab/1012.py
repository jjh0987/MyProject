import sys
input = sys.stdin.readline
limit_number = 30000
sys.setrecursionlimit(limit_number)
query = int(input())
# query_map = []
def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    elif mapping[x][y] == 1:
        mapping[x][y] = 0
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True

for _ in range(query):
    m,n,k = map(int,input().split())
    mapping = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        mapping[y][x] = 1
    # query_map.append(mapping)
    ans = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                ans += 1
    print(ans)


