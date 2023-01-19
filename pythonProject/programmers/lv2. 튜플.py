s = "{{123}}"
s = s.split('{')
target = []
for i in s:
    tp = []
    j = 0
    while j < len(i):
        tar = ''
        while 1:
            if i[j] == ',' or i[j] == '}':
                break
            tar += i[j]
            j += 1
        if tar:
            tp.append(eval(tar))
        j += 1
    if tp:
        target.append(tp)

ans = sorted([[len(i),i] for i in target])
answer = ans[0][1]
for i in range(1,len(ans)):
    tp = set(ans[i-1][1])
    for j in ans[i][1]:
        if j not in tp:
            answer.append(j)
            break

