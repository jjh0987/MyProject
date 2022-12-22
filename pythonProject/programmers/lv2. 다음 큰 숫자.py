n = 78

tar = list(bin(n)[2:])

ans = ''
if tar.count('0') == 0:
    for i in range(len(tar)+1):
        if i != 1:
            ans += tar[i]
        elif i == 1:
            ans += '0'
else:
    for i in range(1,len(tar)):
        if i == 1:
            continue
        if tar[i-1] == '1' and tar[i] == '0':
            tar[i-1] = '0'
            tar[i] = '1'
        elif tar[i-1] == '0' and tar[i] == '1':
            tar[i-1] = '1'
            tar[i] = '0'
