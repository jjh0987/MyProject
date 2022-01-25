def star(k):
    if k > 3:
        temp = star(k/3)*3
        setting = []
        for i in temp:
            setting.append(i*3)
        i = 0
        while i < k:
            j = 0
            tem_s = ''
            while j < k:
                if i//(k/3) == 1:
                    if j//(k/3) == 1:
                        tem_s += ' '
                    else:
                        tem_s += setting[i][j]
                else:
                    tem_s += setting[i][j]
                j += 1
            if i//(k/3) == 1:
                setting[i] = tem_s
            i += 1
        return setting
    elif k == 3: return ['***','* *','***']
k = int(input())
for i in star(k):
    print(i)