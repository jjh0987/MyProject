skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

target = []
for tree in skill_trees:
    tp = []
    for s in tree:
        if s in skill:
            tp.append(skill.index(s))
    target.append(tp)

id_target = []
for i in target:
    flag = 0
    for j in range(len(i)):
        if i[j] != j:
            flag = 1
    id_target.append(flag)

id_target.count(1)