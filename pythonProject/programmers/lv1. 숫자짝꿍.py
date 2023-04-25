X = '5525'
Y = '1255'


def solution(X, Y):
    from collections import Counter
    X = Counter(X)
    Y = Counter(Y)

    target = {f'{i}': 0 for i in range(10)}
    for i in X:
        target[i] += min(X[i], Y[i])

    answer = ''
    for i in reversed(target):
        if target[i] == 0:
            continue
        else:
            answer += target[i] * i

    if not answer:
        return '-1'

    if list(set(answer))[0] == '0' and len(set(answer)) == 1:
        return '0'

    if answer:
        return answer