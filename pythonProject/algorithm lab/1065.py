def solve(x):
    if len(x) == 1:
        return 1
    target = [int(i) for i in ','.join(x).split(',')]
    i = 0
    ans = []
    while 1:
        try:
            temp = target[i] - target[i+1]
            ans.append(temp)
            i += 1
        except:
            break
    if len(set(ans)) == 1:
        return 1
    else:
        return 0

cnt = 0
for i in range(1,int(input())+1):
    cnt += solve(str(i))
print(cnt)