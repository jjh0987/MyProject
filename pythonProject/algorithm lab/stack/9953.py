s = input()
tar = input()

stack = []
for i in s:
    stack.append(i)
    if ''.join(stack[-len(tar):]) == tar:
        del stack[-len(tar):]

ans = ''.join(stack)
if not ans:
    print('FRULA')
else:
    print(ans)