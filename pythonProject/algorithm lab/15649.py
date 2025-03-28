import sys
input = sys.stdin.readline
n,m = map(int,input().split())
answer = []
visited = [False for _ in range(n+1)]
def back():
    if len(answer) == m:
        print(*answer)
    for i in range(1,n+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            back()
            answer.pop()
            visited[i] = False
back()