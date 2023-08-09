p = int(input())
ans = [0,0,0,0]
for i in range(p):
    tar = list(map(int,input().split()))
    if tar[0] >= 2:
        if tar[1] == 1 or tar[1] == 2:
            ans[0] += 1
        elif tar[1] == 3:
            ans[1] += 1
        elif tar[1] == 4:
            ans[2] += 1
        else:
            ans[3] += 1
    else:
        ans[3] += 1

print(*ans,sep='\n')

1
11
12
1121
122111
112213
12221131
1123123111

n = int(input())-1
if n <= 6:
    def counter(target):
        target = list(target)
        stack = []
        while target:
            tar = target.pop()
            stack.append(tar)
            if len(set(stack)) == 2:
                stack.pop()
                break
        return stack

    target = '1'
    for _ in range(n):
        ans = []
        while target:
            ans.append(counter(target))
            target = target[:-len(ans[-1])]
        ans.reverse()
        for i in range(len(ans)):
            target = target + ans[i][0] + str(len(ans[i]))
    print(max(list(target)))
else:
    print(3)
