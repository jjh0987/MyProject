n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

scores = [i for i in range(10,-1,-1)]

target = []
for i in range(1,11):
    tar = [0] * 11
    tar_n = n
    for j in range(11):
        if tar_n > info[j] + 1:
            tar[j] = info[j] + 1
            tar_n -= info[j] + 1
        # elif tar_n == info[j]:
        #     try:
        #         tar[j+1] = tar_n
        #     except:pass
        #     tar_n = 0
        if tar_n < 0:
            break

    target.append(tar)
target
answer = []
for j in range(len(target)):
    rian = 0
    peach = 0
    for i in range(len(info)):
        if info[i] < target[j][i]:
            rian += scores[i]
        elif info[i] >= target[j][i] and info[i] != 0:
            peach += scores[i]
    if rian != 0:
        answer.append(rian)

if answer:
    answer = target[answer.index(max(answer))]
else:
    answer = [-1]
print(answer)
target