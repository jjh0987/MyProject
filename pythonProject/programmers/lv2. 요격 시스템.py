target = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
target.sort(key=lambda x:x[1])
target = [[i[0],i[1]-1] for i in target]
ans = 0
i = 0

while i < len(target):
    tmp = target[i][1]
    try:
        while tmp >= target[i+1][0] and tmp <= target[i+1][1]:
            i += 1
    except:
        ans += 1
        break
    i += 1
    ans += 1

target