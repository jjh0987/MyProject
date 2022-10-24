import sys
input = sys.stdin.readline
n = int(input())

stack = []
stack_set = set()
ans = []
def push():
    tp = stack.pop()
    stack_set.remove(tp)
    ans.append('+')
def stack_pop():
    tp = tar.pop()
    stack.append(tp)
    stack_set.add(tp)
    ans.append('-')

tar = [int(input()) for _ in range(n)] # -> reverse range n
flag = 0
# 역순수열로 복원시키기
while n > 0:
    tar = int(input())
    try:
        if n not in stack_set:
            while n not in stack_set:
                stack_pop()

        if n in stack_set:
            while n in stack_set:
                push()
        n -= 1
    except:
        flag = 1

if flag == 0:
    for i in range(len(ans)-1,-1,-1):
        print(ans[i])
else:
    print('NO')
