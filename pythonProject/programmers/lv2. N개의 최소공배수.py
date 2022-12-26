arr = [i for i in range(1,1001)]
arr = list(set(arr))
import math
def prime(x):
    if x == 1:
        return
    elif x == 2:
        return 2
    for j in range(2, int(math.sqrt(x)) + 2):
        if x % j == 0:
            return
    return x

nums = []
for i in range(1,1001):
    if prime(i):
        nums.append(prime(i))

mapping = [[0]*len(nums) for _ in range(len(arr))]
for i in range(len(arr)):
    while arr[i] != 1:
        for j in range(len(nums)):
            if arr[i]%nums[j] == 0:
                mapping[i][j] += 1
                arr[i] = int(arr[i]/nums[j])
                break

answer = 1
for j in range(len(nums)):
    answer *= nums[j]**max([mapping[i][j] for i in range(len(arr))])
answer
