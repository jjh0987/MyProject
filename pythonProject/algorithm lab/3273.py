import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
nums.sort()
m = int(input())

i = 0
j = n-1
ans = 0
while i < j:
    tp = nums[i]+nums[j]
    if tp == m:
        ans += 1
        i += 1
        j -= 1
    elif tp > m:
        j -= 1
    else:
        i += 1
print(ans)