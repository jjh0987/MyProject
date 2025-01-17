import sys
input = sys.stdin.readline

i = 1
while 1:
    s = input().rstrip('\n')
    if '-' in s:
        break
    s = list(s)
    stack = []
    cnt = 0
    while s:
        tar = s.pop()
        if tar == '}':
            stack.append(tar)
        else:
            if stack:
                stack.pop()
            else:
                stack.append('}')
                cnt += 1
    print(f'{i}. {cnt+len(stack)//2}')
    i += 1                                                                