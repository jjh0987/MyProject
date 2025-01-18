import sys
import string
import collections
input = sys.stdin.readline
T = int(input())
words = [input().rstrip('\n') for _ in range(T)]
words.sort()