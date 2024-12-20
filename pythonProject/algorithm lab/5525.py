import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip('\n')

pn = []
i = 0
while i < m-2*n:
    if s[i] == 'I':
        tp = 0
        while 1:
            if s[i+1:i+3] == 'OI':
                i += 2
                tp += 1
            else:
                break
        pn.append(tp)
    i += 1

pn = [i-n for i in pn if i-n >= 0]
answer = len(pn) + sum(pn)
print(answer)