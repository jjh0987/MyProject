s = "1111111"

cnt1 = 0
cnt2 = 0
while s != '1':
    if '0' in s:
        cnt1 += s.count('0')
        s = ''.join(s.split('0'))
    else:
        s = bin(len(s))[2:]
        cnt2 += 1

print(cnt2+1,cnt1)