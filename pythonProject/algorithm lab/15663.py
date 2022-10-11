import sys
input = sys.stdin.readline
n,m = map(int,input().split())
target = list(map(int,input().split()))
target.sort()
import itertools
tar = sorted(list(set(itertools.permutations(target,m))))
for i in tar:
    print(*i)