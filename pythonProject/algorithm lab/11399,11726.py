# 11399
n = int(input())
time_seq = list(map(int,input().split()))
time_seq.sort()
time_seq.reverse()
ans = 0
for i in range(n,0,-1):
    ans += time_seq[i-1]*i

print(ans)

# 11726
n = int(input())

if n == 1:
    start = [1]
elif n == 2:
    start = [2]
else:
    start = [1, 2]
    while len(start) != n:
        start.append(start[-1]+start[-2])

print(start[-1]%10007)