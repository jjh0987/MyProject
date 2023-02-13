files = ["F-5abab5 ", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

from string import ascii_uppercase
from string import ascii_lowercase

alphabet_list = list(ascii_uppercase)
alphabet_list.extend(ascii_lowercase)
alphabet_list.extend([' ','.','-'])
number_list = [str(i) for i in range(10)]

from collections import deque
def slicer(string):
    string = deque(string)
    HEAD = ''
    while 1:
        tar = string.popleft()
        if tar in alphabet_list:
            HEAD += tar
        else:
            string.appendleft(tar)
            break
    NUMBER = ''
    while 1:
        tar = string.popleft()
        if tar in number_list:
            if len(NUMBER) > 5:
                string.appendleft(tar)
                break
            NUMBER += tar
        else:
            string.appendleft(tar)
            break

    TAIL = ''
    while string:
        try:
            tar = string.popleft()
            TAIL += tar
        except:
            break
    return [HEAD,NUMBER,TAIL]

target = [[slicer(files[i]),i] for i in range(len(files))]

from copy import deepcopy
confirm = [[['','0'],0]]
confirm.extend(deepcopy(target))

for i in confirm:
    try:
        i[0][0] = i[0][0].lower()
        i[0][1] = int(i[0][1].lstrip('0'))
        i[0].pop()
    except:pass
confirm.sort()
x = 0
for i in range(1,len(confirm)):
    if confirm[i-1][0] != confirm[i][0]:
        x += 1
    confirm[i].append(x)
tp = [[i[1],i[2]] for i in confirm[1:]]
tp.sort(key=lambda x:x[0])

for i in range(len(tp)):
    if target[i][1] == tp[i][0]:
        target[i].append(tp[i][1])

target.sort(key=lambda x:x[2])
[''.join(i[0]) for i in target]


files = ["F-5abab5 ", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

import re

def slicer(string):
    reg = f'[a-zA-Z .-]+'
    p = re.compile(reg)
    tp = p.match(string).span()
    HEAD = string[tp[0]:tp[1]]
    string = string[tp[1]:]

    reg = f'[0-9]+'
    p = re.compile(reg)
    tp = list(p.match(string).span())
    if tp[1] > 5:
        tp[1] = 5

    NUMBER = string[tp[0]:tp[1]]
    TAIL = string[tp[1]:]

    return [HEAD,NUMBER,TAIL]

target = [slicer(files[i]) for i in range(len(files))]
target.sort(key=lambda x:[x[0].lower(),int(x[1])])
[''.join(i) for i in target]
