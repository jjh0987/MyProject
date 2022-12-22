s = 'baabaa'

s = list(s)
stack = []
while s:
    stack.append(s.pop())
    try:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    except:
        pass

