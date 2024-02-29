import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())
b21 = list(map(int, input().split()))
b22 = list(map(int, input().split()))
b21.sort()
b22.sort()

answer = []
if n % 2 == 1:
    answer.append(b21.pop())
    n -= 1

flag = 0
while 1:
    if n == 0:
        break
    if len(b21) < 2:
        flag = 1
        break
    if len(b22) < 1:
        flag = 2
        break

    b21_a = b21.pop()
    b21_b = b21.pop()
    b22_a = b22.pop()
    if b22_a >= b21_a + b21_b:
        answer.append(b22_a)
        b21.append(b21_a)
        b21.append(b21_b)
        n -= 2
    else:
        answer.append(b21_a)
        answer.append(b21_b)
        b22.append(b22_a)
        n -= 2

if flag == 1:
    while n > 0:
        answer.append(b22.pop())
        n -= 2
elif flag == 2:
    while n > 0:
        answer.append(b21.pop())
        answer.append(b21.pop())
        n -= 2

print(sum(answer))                        