s = "aukks"
skip = "wbqd"
index = 5

from string import ascii_lowercase
alphabet_list = set(list(ascii_lowercase))
skip = set(list(skip))
alphabet_list = list(alphabet_list.difference(skip))
alphabet_list.sort()

answer = ''
for i in s:
    new_idx = alphabet_list.index(i)+index
    answer += alphabet_list[new_idx%len(alphabet_list)]

answer