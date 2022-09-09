def solution(str1, str2):
    tp1 = []
    for i in range(len(str1)):
        try:
            tp1.append(f'{str1[i].upper()}{str1[i + 1].upper()}')
        except:
            pass

    tp2 = []
    for i in range(len(str2)):
        try:
            tp2.append(f'{str2[i].upper()}{str2[i + 1].upper()}')
        except:
            pass

    import re

    tp1 = [re.sub(r'[^A-Z]', '', i) for i in tp1]
    tp2 = [re.sub(r'[^A-Z]', '', i) for i in tp2]

    str1_set = []
    str2_set = []
    for i in tp1:
        if len(i) == 2:
            str1_set.append(i)
    for i in tp2:
        if len(i) == 2:
            str2_set.append(i)

    key_bundle = set(str1_set).union(set(str2_set))
    ans_union = dict()
    ans_inter = dict()
    import collections
    tar1 = collections.Counter(str1_set)
    tar2 = collections.Counter(str2_set)

    for key in key_bundle:
        ans_union[key] = max(tar1[key], tar2[key])
        ans_inter[key] = min(tar1[key], tar2[key])

    try:
        return int(sum(ans_inter.values()) / sum(ans_union.values()) * 65536)
    except:
        return 65536


solution('E=M*C^2','e=m*c^2')

str1 = 'handshake'
str2 = 'shake hands'
tp1 = []
for i in range(len(str1)):
    try:
        tp1.append(f'{str1[i].upper()}{str1[i + 1].upper()}')
    except:
        pass

tp2 = []
for i in range(len(str2)):
    try:
        tp2.append(f'{str2[i].upper()}{str2[i + 1].upper()}')
    except:
        pass
tp2

import re

tp1 = [re.sub(r'[^A-Z]', '', i) for i in tp1]
tp2 = [re.sub(r'[^A-Z]', '', i) for i in tp2]

str1_set = []
str2_set = []
for i in tp1:
    if len(i) == 2:
        str1_set.append(i)
for i in tp2:
    if len(i) == 2:
        str2_set.append(i)

key_bundle = set(str1_set).union(set(str2_set))
ans_union = dict()
ans_inter = dict()
import collections

tar1 = collections.Counter(str1_set)
tar2 = collections.Counter(str2_set)

for key in key_bundle:
    ans_union[key] = max(tar1[key], tar2[key])
    ans_inter[key] = min(tar1[key], tar2[key])

sum(ans_inter.values()) / sum(ans_union.values()) * 65536

str1_set
str2_set