import sys

data = {'(',')','[',']'}
while 1:
    temp = sys.stdin.readline()
    if temp == '.\n':
        break
    else:
        ans = []
        for i in temp:
            if i in data:
                ans.append(i)
        if len(ans) == 0:
            print('yes')
        else:
            target = ''
            for i in ans:
                target += i
            while len(target) != 0:
                test1 = len(target)
                target = target.replace('()','')
                target = target.replace('[]','')
                if test1 == len(target):
                    break
            if len(target) == 0:
                print('yes')
            else:
                print('no')
