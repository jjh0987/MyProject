import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

item = sorted(list(map(int,input().split())))
i = 0
j = n-1
cnt = 0
while i < j:
    if item[i]+item[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif item[i]+item[j] < m:
        i += 1
    elif item[i]+item[j] > m:
        j -= 1

print(cnt)