import sys
input = sys.stdin.readline
n = int(input())
seq = list(map(int,input().split()))

stack = []
answer = []
while seq:
    if not stack:
        stack.append(seq.pop())
        answer.append(-1)
        continue
    stack.append(seq.pop())
    if stack[-2] > stack[-1]:
        answer.append(stack[-2])
    else:
        try:
            tar = stack.pop()
            while stack[-1] <= tar:
                stack.pop()
            answer.append(stack[-1])
            stack.append(tar)
        except:
            answer.append(-1)
            stack.append(tar)

answer.reverse()
print(*answer)
