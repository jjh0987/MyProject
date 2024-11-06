n,m = map(int,input().split())
graph = [[1 for _ in range(m)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,m):
        graph[i][j] = (graph[i-1][j] + graph[i][j-1] + graph[i-1][j-1])%1000000007

print(graph[n-1][m-1])
