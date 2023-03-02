keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

import string
alpha = list(string.ascii_uppercase)
alpha_min = {i:100 for i in alpha}

for alp in alpha:
    tp = []
    for key in keymap:
        try:
            tp.append(key.index(alp)+1)
        except:
            pass
    if tp:
        alpha_min[alp] = min(min(tp),alpha_min[alp])


ans = []
for i in targets:
    flag = 0
    tp = 0
    for s in i:
        if alpha_min[s] == 100:
            flag = 1
            break
        tp += alpha_min[s]
    if flag == 1:
        ans.append(-1)
    else:
        ans.append(tp)
