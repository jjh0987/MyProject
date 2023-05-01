sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5


import collections
sequence_co = collections.Counter(sequence)
target = [i*sequence_co[i] for i in sequence_co.keys()]

target

temp = 0
i = 1
while k > temp:
    step = target[len(target)-i]
    temp += step
    i -= 1

start = target.index(step)