numbers = [2,7]

def find(x):
    i = 1
    tp1 = bin(x)[2:]

    if x%2 == 0:
        tp1 = tp1[:-1] + '1'
        return int(tp1,2)

    while 1:
        diff = 0
        tp2 = bin(x+i)[2:]
        if len(tp2) > len(tp1):
            tp3 = '0' + tp1
        else:
            tp3 = tp1

        for j in range(len(tp3)):
            if diff > 2:
                break
            if tp2[j] != tp3[j]:
                diff += 1

        if diff <= 2:
            break

        i += 1
    return int(tp2,2)

label = [find(i) for i in range(100001)]
answer = [label[i] for i in numbers]
label[100000]

find(3)

bin(3)
bin(4)