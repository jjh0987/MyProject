numbers = [9, 1, 5, 3, 7, 2, 2]
# [-1, 5, 6, 6, -1, -1, -1]
ans = [-1]*len(numbers)
M = 0
flag = 0
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        ans[i] = numbers[i+1]
        if numbers[0] > M:
            M = max(M,numbers[i+1])
        else:
            ans[0] = M
            flag = 1

i = -1
while i < len(numbers):
    try:
        if ans[i] != -1:
            while 1:
                i -= 1
                ans[i] = ans[i+1]
                if ans[i] != ans[i-1]:
                    break
        i -= 1
    except:
        break

if flag == 0:
    ans[0] = -1