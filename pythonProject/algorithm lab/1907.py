import sys
input = sys.stdin.readline
s = input().rstrip('\n')
target = s.split('+')
tar = target.pop()
target.extend(tar.split('='))

cnt = dict()
for i in range(3):
    tar = target[i]
    tp = {'C':0,
          'H':0,
          'O':0}
    for j in range(len(tar)):
        if tar[j] not in {'C','H','O'}:
            continue
        try:
            tp[tar[j]] += int(tar[j+1])
        except:
            tp[tar[j]] += 1
    cnt[i] = tp

flag = False
for x1 in range(1,11):
    for x2 in range(1,11):
        for x3 in range(1,11):
            M1 = cnt[0]
            M2 = cnt[1]
            M3 = cnt[2]
            tp = 0
            for key in M1:
                if M1[key]*x1+M2[key]*x2 == M3[key]*x3:
                    tp += 1
            if tp == 3:
                flag = True
                print(x1,x2,x3)
                break
        if flag:
            break
    if flag:
        break