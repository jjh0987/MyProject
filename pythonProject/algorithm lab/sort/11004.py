import sys
input = sys.stdin.readline
a,b = map(int,input().split())
tar = sorted(list(map(int,input().split())))
print(tar[b-1])
