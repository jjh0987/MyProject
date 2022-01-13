# 범위 주석 ctrl + / 범위 들여쓰기 tap , shift tap
i = 0
q = int(input())
test = []
while i < 18:
    test.append((10**(i+1)-10**i)*(i+1))
    i += 1
j = 0
while j < q:
    k = int(input())
    for x in test:
        if k < 0:
            k += test[test.index(x)-1]
            loc = test.index(x) #자리수
            break
        else:
            k -= x
    val,rem = divmod(k,loc)
    ans = (10 ** (loc - 1) - 1) + val
    if rem == 0:
        print(str(ans)[-1])
        j += 1
    else:
        print(str(ans+1)[rem-1])
        j += 1

