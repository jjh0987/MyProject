import sys
li = [0]*10001
for i in range(int(input())):
    li[int(sys.stdin.readline())] += 1

a = -1
for i in li:
    a += 1
    for j in range(i):
        print(a)