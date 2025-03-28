import sys
input = sys.stdin.readline
n,m = map(int,input().split())
nums = list(map(int,input().split()))

i = 0
j = 0
ans = 0
cnt = nums[0]
while j < n:
    try:
        if cnt < m:
            j += 1
            cnt += nums[j]
        elif cnt == m:
            cnt -= nums[i]
            ans += 1
            i += 1
        while cnt > m:
            cnt -= nums[i]
            i += 1
            if cnt == m:
                ans += 1
                j += 1
                cnt += nums[j]
    except:print(ans)

