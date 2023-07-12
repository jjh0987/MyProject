name = "JAN"

import re
p = re.compile('[B-Z]+')
len_a = [len(i) for i in p.split(name)]

from string import ascii_uppercase
alpha = {ascii_uppercase[i]:i for i in range(len(ascii_uppercase))}
rev_alpha = {ascii_uppercase[i]:26-i for i in range(len(ascii_uppercase))}

def updown_min(alp):
    return min(rev_alpha[alp],alpha[alp])

ans = 0
target = [updown_min(i) for i in name]
i = 0
k = 0

conf1 = target[(i-k)%len(target)]
conf2 = target[(i+k)%len(target)]
stop = sum(target)
while stop > 0:
    ans += target[i]
    stop -= target[i]
    target[i] = 0
    if conf1 == 0 and conf2 == 0:
        k += 1
        continue
    if max(conf1,conf2) == conf1:
        i -= 1
        k = 0
    elif max(conf1,conf2) == conf2:
        i -= 1
        k = 0
    ans += 1

ans-1
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