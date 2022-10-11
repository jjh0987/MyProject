import sys
input = sys.stdin.readline
n,m = map(int,input().split())
target = list(set(map(int,input().split())))
target.sort()
import itertools
tar = sorted(list(set(itertools.combinations_with_replacement(target,m))))
for i in tar:
    print(*i)