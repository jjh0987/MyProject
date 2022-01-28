n = int(input())
temp = int(input())
if n == 1:
    print(temp)
else:
    start = [int(i) + temp for i in input().split()]
    for i in range(n - 2):
        start.append(0)
    if n == 2:
        print(max(start))
    else:
        for i in range(n-2):
            target = [int(k) for k in input().split()]
            temp = [0]*n
            for j in range(len(target)):
                if j == 0:
                    temp[j] = start[j] + target[j]
                elif j == len(target):
                    temp[j] = start[j-1] + target[j]
                else:
                    temp[j] = max(start[j] + target[j], start[j-1] + target[j])
            start = temp
        print(max(start))