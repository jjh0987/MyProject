N = int(input())
S = input()
Q = int(input())

num = list(range(10))
op = ['+','-']
for i in range(Q):
    tempS = S
    temp = list(map(str,input().split()))
    if temp[0] == '1':
        S = S.replace(S[int(temp[1])-1:int(temp[2])],temp[3])
    else:
        tempS = tempS[int(temp[1])-1:int(temp[2])]
        temp_c = []
        for i in tempS:
            try:
                temp_c.append(eval(i))
            except:
                temp_c.append(i)
        i = 0
        part = '0'
        ans = 0
        temp_c.append('+')
        while 1:
            try:
                if temp_c[i] == '+':
                    while 1:
                        i += 1
                        if temp_c[i] in op:
                                part.lstrip('0')
                                ans += int(part)
                                part = '0'
                                break
                        part += str(temp_c[i])
                elif temp_c[i] == '-':
                    while 1:
                        i += 1
                        if temp_c[i] in op:
                            part.lstrip('0')
                            ans -= int(part)
                            part = '0'
                            break
                        part += str(temp_c[i])
                else:
                    while 1:
                        if temp_c[i] in op:
                            part.lstrip('0')
                            ans += int(part)
                            part = '0'
                            break
                        part += str(temp_c[i])
                        i += 1
            except:
                print(ans%(10**9+7))
                break


N = int(input())
S = input()
Q = int(input())

op = ['+','-']
for i in range(Q):
    tempS = S
    temp = list(map(str,input().split()))
    for i in range(3):
        temp[i] = int(temp[i])
    if temp[0] == 1:
        S = S.replace(S[temp[1]-1:temp[2]],temp[3])
    else:
        tempS = tempS[temp[1]-1:temp[2]]
        ans = 0
        part = '0'
        i = 0
        while i < temp[2]-temp[1]+1:
            part = '0'
            if tempS[i] == '+':
                i += 1
                try:
                    while tempS[i] not in op:
                        part += tempS[i]
                        i += 1
                except:pass
                ans += int(part)
            elif tempS[i] == '-':
                i += 1
                try:
                    while tempS[i] not in op:
                        part += tempS[i]
                        i += 1
                except:pass
                ans -= int(part)
            else:
                try:
                    while tempS[i] not in op:
                        part += tempS[i]
                        i += 1
                except:pass
                ans += int(part)
        print(ans%(10**9+7))

N = int(input())
S = input()
Q = int(input())

import re

for i in range(Q):
    tempS = S
    temp = list(map(str,input().split()))
    for i in range(3):
        temp[i] = int(temp[i])
    if temp[0] == 1:
        S = S.replace(S[temp[1]-1:temp[2]],temp[3])
    else:
        tempS = '+'+tempS[temp[1]-1:temp[2]]
        p = re.compile('[+,-][0-9]*')
        l1 = p.findall(tempS)
        ans = 0
        for i in l1:
            if len(i) == 1:
                continue
            ans += int(i)
        print(ans%(10**9+7))