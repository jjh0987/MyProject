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
