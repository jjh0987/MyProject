import sys

input = sys.stdin.readline

n = int(input())
fibo = [0, 1]
while 1:
    tar = fibo[-2] + fibo[-1]
    if tar < 1000000000:
        fibo.append(tar)
    else:
        break

for _ in range(n):
    tar = int(input())
    tp = []
    for i in range(1, len(fibo)):
        if tar - fibo[-i] >= 0:
            tp.append(fibo[-i])
            tar = tar - fibo[-i]
    print(*sorted(tp))                    