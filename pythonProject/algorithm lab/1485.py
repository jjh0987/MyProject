import sys
input = sys.stdin.readline
n = int(input())
square = []
for i in range(n):
    tp = []
    for j in range(4):
        tp.append(list(map(int,input().split())))
    square.append(tp)