import itertools
import math
def solution(number):

    tp = []
    for i in range(1,len(number)+1):
        tp.extend(list(itertools.permutations(number,i)))

    tar = [int(''.join(i)) for i in tp]
    tar = list(set(tar))

    def prime(x):
        if x == 1:
            return
        elif x == 2:
            return 2
        for j in range(2, int(math.sqrt(x)) + 2):
            if x % j == 0:
                return
        return x
    cnt = 0
    for num in tar:
        if prime(num):
            cnt += 1
    return cnt