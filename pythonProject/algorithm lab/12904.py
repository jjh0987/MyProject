S = input()
T = list(input())
s = len(S)

while 1:
    tar = T.pop()
    if tar == 'B':
        T.reverse()
    if s == len(T):
        break
if S == ''.join(T):
    print(1)
else:
    print(0)                        