name = "JEROEN"

name = name.split('A')
name

from string import ascii_uppercase
alpha = {ascii_uppercase[i]:i for i in range(len(ascii_uppercase))}
rev_alpha = {ascii_uppercase[i]:26-i for i in range(len(ascii_uppercase))}

def updown_min(alp):
    return min(rev_alpha[alp],alpha[alp])

ans = 0
for i in name:
    ans += sum([updown_min(j) for j in i])
ans += len(name)-1


# answer0 = 0
# i = 0
# while i < len(name):
#     answer0 += updown_min(name[i])
#     if name[i:] == 'A'*(len(name)-i):
#         print('hi')
#     else:
#         answer0 += 1
#     i += 1
#
# answer1 = 0
# i = 0
# while i < len(name):
#     answer1 += updown_min(name[-i])
#     if name[:i] == 'A'*(len(name)-i):
#         break
#     else:
#         answer1 += 1
#     i += 1
#
# min(answer0-1,answer1-1)