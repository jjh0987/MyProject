n = 16

# 110 -> 1001 case


tar = list(bin(n)[2:])

flag = 0
check = 0
for i in tar:
    if i == '1':
        check += 1
    if tar[check:].count('1') == 0:
        flag = 1
        break
    if len(tar[check:]) == 0:
        flag = 0

ans = ''

if n in [2**i for i in range(1,20)]:
    tar.append('0')
    ans = ''.join(tar)
elif flag == 1:
    ans = '1'
    for i in range(len(tar)-1):
        ans += '0'
    ans += '1'
elif tar.count('0') == 0:
    ans = '10'
    for _ in range(len(tar) - 1):
        ans += '1'
else:
    tar.reverse()
    for i in range(1,len(tar)):
        if tar[i-1] == '1' and tar[i] == '0':
            tar[i-1] = '0'
            tar[i] = '1'
            marking = i
            break
    try:
        for i in range(1,marking-1):
            if tar[i-1] == '0' and tar[i] == '1':
                tar[i-1] = '1'
                tar[i] = '0'
    except:pass
    tar.reverse()
    ans = ''.join(tar)

int(ans,2)



n = 78
tar = bin(n)[2:]
check = tar.count('1')
while 1:
    n += 1
    if bin(n)[2:].count('1') == check:
        break
