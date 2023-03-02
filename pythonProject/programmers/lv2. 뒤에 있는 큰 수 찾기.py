<<<<<<< HEAD
numbers = [9, 2, 1, 5, 3, 6, 2]

stack = []
ans = [-1]


while 1:
    tar = numbers.pop()
    stack.append(tar)
    try:
        if tar > numbers[-1]:
            numbers.append(stack.pop())
            stack.reverse()
            while stack:
                if ans[-1] != -1:
                    ans.append(max(ans[-1],stack.pop()))
                else:
                    stack.pop()
                    ans.append(-1)
            break
    except:
        stack.reverse()
        while stack:
            if ans[-1] != -1:
                ans.append(max(ans[-1], stack.pop()))
            else:
                stack.pop()
                ans.append(-1)
        break

while 1:
    tar = numbers.pop()
    stack.append(tar)
    if tar <= numbers[-1]:
        numbers.append(stack.pop())
        while stack:
            ans.append(stack.pop())
        break
=======
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
>>>>>>> e7a64fd42fbe7990b171b1d713002f51ebf70793
