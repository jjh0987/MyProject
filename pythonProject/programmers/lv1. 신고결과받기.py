id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

mail = dict()
danger = dict()
ans = dict()
for id in id_list:
    mail[id] = set()
    danger[id] = set()
    ans[id] = 0

for re in report:
    a,b = re.split()
    mail[a].add(b)
    danger[b].add(a)

for i in danger:
    danger[i] = len(danger[i])

target = []
for i in danger:
    if danger[i] >= k:
        target.append(i)

for i in mail:
    for j in target:
        if j in mail[i]:
            ans[i] += 1
list(ans.values())
