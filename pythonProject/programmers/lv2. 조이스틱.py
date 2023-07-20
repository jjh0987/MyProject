name = "BBBBAAAABA" # 10
# import re
# p = re.compile('[B-Z]+')
# len_a = [len(i) for i in p.split(name)]

from string import ascii_uppercase
alpha = {ascii_uppercase[i]:i for i in range(len(ascii_uppercase))}
rev_alpha = {ascii_uppercase[i]:26-i for i in range(len(ascii_uppercase))}

def updown_min(alp):
    return min(rev_alpha[alp],alpha[alp])

ans = 0
target = [updown_min(i) for i in name]
i = 0
k = 1

stop = sum(target)
while stop > 0:
    stop = sum(target)
    conf1 = target[(i - k) % len(target)]
    conf2 = target[(i + k) % len(target)]
    if target[i] != 0:
        ans += target[i]
        target[i] = 0
    if conf1 == conf2:
        k += 1
    elif conf1 >= conf2:
        stop -= target[i]
        ans += 1
        i -= 1
        k = 1
    elif conf1 < conf2:
        stop -= target[i]
        ans += 1
        i += 1
        k = 1

ans
# answer0 = 0
# i = 0
# while i < len(name):
#     answer0 += updown_min(name[i])
#     if name[i:] == 'A'*(len(name)-i):
#         print('hi')
#     else:
#         answer0 += 1
#     i += 1
#
# answer1 = 0
# i = 0
# while i < len(name):
#     answer1 += updown_min(name[-i])
#     if name[:i] == 'A'*(len(name)-i):
#         break
#     else:
#         answer1 += 1
#     i += 1
#
# min(answer0-1,answer1-1)


def solution(name):
    from string import ascii_uppercase
    alpha = {ascii_uppercase[i]: i for i in range(len(ascii_uppercase))}
    rev_alpha = {ascii_uppercase[i]: 26 - i for i in range(len(ascii_uppercase))}

    def updown_min(alp):
        return min(rev_alpha[alp], alpha[alp])

    ans = 0
    target = [updown_min(i) for i in name]
    i = 0
    k = 1

    while 1:
        stop = sum(target)
        if stop == 0:
            break
        conf1 = target[(i - k) % len(target)]
        conf2 = target[(i + k) % len(target)]
        if target[i] != 0:
            ans += target[i]
            target[i] = 0
        if conf1 == 0 and conf2 == 0:
            k += 1
        elif conf1 >= conf2:
            stop -= target[i]
            ans += 1
            i -= 1
            k = 1
        elif conf1 < conf2:
            stop -= target[i]
            ans += 1
            i += 1
            k = 1

    ans1 = 0
    target = [updown_min(i) for i in name]
    i = 0
    k = 1

    while 1:
        stop = sum(target)
        if stop == 0:
            break
        conf1 = target[(i - k) % len(target)]
        conf2 = target[(i + k) % len(target)]
        if target[i] != 0:
            ans1 += target[i]
            target[i] = 0
        if conf1 == 0 and conf2 == 0:
            k += 1
        elif conf1 > conf2:
            stop -= target[i]
            ans1 += 1
            i -= 1
            k = 1
        elif conf1 <= conf2:
            stop -= target[i]
            ans1 += 1
            i += 1
            k = 1

    ans_list = []
    for i in range(-len(name)//2,len(name)//2+1):
        ans2 = abs(i)
        target = [updown_min(j) for j in name]
        k = 1

        while 1:
            stop = sum(target)
            if stop == 0:
                break
            i = i % (len(target))
            conf1 = target[(i - k) % len(target)]
            conf2 = target[(i + k) % len(target)]
            if target[i] != 0:
                ans2 += target[i]
                target[i] = 0
            if conf1 == 0 and conf2 == 0:
                k += 1
            elif conf1 > conf2:
                stop -= target[i]
                ans2 += 1
                i -= 1
                k = 1
            elif conf1 <= conf2:
                stop -= target[i]
                ans2 += 1
                i += 1
                k = 1
        ans_list.append(ans2)

    return min(min(ans_list),min(ans, ans1))
solution(name)
name