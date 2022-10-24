ans = list(map(int,input()))
ans.sort(reverse=True)

answer = ''
for i in ans:
    answer += str(i)
print(answer)


import sys
input = sys.stdin.readline
a,b = map(int,input().split())
tar = sorted(list(map(int,input().split())))
print(tar[b-1])
