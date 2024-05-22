import sys
input = sys.stdin.readline

n = int(input())
q = list(map(int,input().split()))

nums = [i for i in range(1,n+1)]
arr = [1]
for i in range(1,n+1):
    arr.append(i*arr[-1])
step = int(n)
if q[0] == 1:
    k = q[1]
    answer = []
    while nums:
        mul = k//arr[step-1]
        if k%arr[step-1] == 0:
            mul -= 1
        answer.append(nums.pop(mul))
        if arr[step-1] <= k:
            k -= arr[step-1]*mul
        step -= 1
    print(*answer)
else:
    k = 1
    import collections
    target = collections.deque(q[1:])
    while nums:
        tar = target.popleft()
        mul = nums.index(tar)
        del nums[mul]
        k += mul*arr[step-1]
        step -= 1
    print(k)