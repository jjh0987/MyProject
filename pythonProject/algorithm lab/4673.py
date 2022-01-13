L = [i for i in range(1,10001)]
ans = []
while L:
    target = str(L.pop(0))
    ans.append(target)
    while 1:
        try:
            temp = 0
            for i in target:
                temp += eval(i)
            target = str(eval(target)+temp)
            del L[L.index(eval(target))]
        except:
            break
for i in ans:
    print(i)

