word = "AAAAE"

alpha = ['A','E','I','O','U']
dictionary = []

from itertools import product
for i in range(1,6):
    dictionary.extend([''.join(i) for i in [i for i in product(alpha,repeat=i)]])
dictionary = sorted(dictionary)
dictionary.index(word)+1

