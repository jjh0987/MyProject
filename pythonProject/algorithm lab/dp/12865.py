import sys
input = sys.stdin.readline
n = int(input())

stack = []
ans = []
def push():
    ans.append(stack.pop())
def stack_pop(a):
    stack.append(a)

tar = [int(input()) for _ in range(n)] # -> reverse range n

# 역순수열로 복원시키기
