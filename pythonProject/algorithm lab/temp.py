import sys
N = int(input())
seq = list(map(int,sys.stdin.readline().split()))
dict = {i:seq[i] for i in range(N)}

dict = {2:1,0:1,1:2}
2 in dict.keys()