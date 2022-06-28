n = int(input())

for n in range(1,41):
    confirm = [3 ** i for i in range(1,18)]
    confirm.reverse()
    ans = []
    print(n)
    for check in confirm:
        tp = n//check
        n -= tp * check
        ans.append(str(tp))
    ans.append(str(n))
    target = ''.join(ans).lstrip('0')
    if target in ['1'*i+'0' for i in range(1,18)]:
        print('4'*(len(target)-1))
    else:
        while '0' in target:
            if '10' in target:
                target = target.replace('10', '03')
            elif '20' in target:
                target = target.replace('20', '13')
            elif '30' in target:
                target = target.replace('30', '23')
            target = target.lstrip('0')

        if '3' in target:
            target = target.replace('3','4')
        print(target)


    #print(ans.lstrip('0'))

