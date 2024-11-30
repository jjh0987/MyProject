import sys
import collections
input = sys.stdin.readline
words = []
for _ in range(6):
    words.append(input().rstrip())

count = collections.Counter(words)
check = set(words)

import itertools
import copy
words = list(itertools.permutations(words,3))

def checking(check_list):
    tp = copy.deepcopy(count)
    for i in check_list:
        tp[i] -= 1
    for i in range(3):
        w = ''.join([w[i] for w in check_list])
        tp[w] -= 1
        if tp[w] < 0:
            return False
        if w not in check:
            return False
    return True

flag = False
for word in words:
    if checking([i for i in word]):
        print(*word,sep='\n')
        flag = True
        break

if not flag:
    print(0)
