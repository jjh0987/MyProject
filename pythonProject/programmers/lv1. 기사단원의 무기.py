number = 10
limit = 3
power = 2
# 리밋을 넘어가면 파워로 대체
# 약수의 개수표
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

tp = [prime(i) for i in range(1,100001)]
prime_table = []
for i in tp:
    if i:
        prime_table.append(i)

ans = [1]
for i in range(2,100001):
    temp = 1
    while i > 1:
        for j in prime_table:
            if j > i:
                break
            if i%j == 0:
                temp += 1
                i /= int(j)
    ans.append(temp)

answer = []
for i in ans[:number]:
    if i > limit:
        answer.append(power)
    else:
        answer.append(i)