import sys
import collections
import string

input = sys.stdin.readline

alphabet = list(string.ascii_uppercase)
s = sorted(input())
s = collections.Counter(s)
cnt = 0
flag = False
left = []
center = ''
right = []

for key in alphabet:
    if s[key] > 0:
        if s[key] == 1:
            if center:
                flag = True
                break
            center += key
        elif s[key] % 2 == 1:
            if center:
                flag = True
                break
            center += key
            tp = s[key] // 2
            left.append(key * tp)
            right.append(key * tp)
        elif s[key] % 2 == 0:
            tp = s[key] // 2
            left.append(key * tp)
            right.append(key * tp)
if flag:
    print("I'm Sorry Hansoo")
else:
    left = ''.join(left)
    right = ''.join(reversed(right))
    print(left + center + right)
