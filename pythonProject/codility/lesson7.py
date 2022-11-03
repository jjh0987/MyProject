# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
S = ')('
def solution(S):
    stack = []
    left = {'{','[','('}
    words = {'U','V','W'}
    try:
        for i in S:
            if i in left:
                stack.append(i)
            elif i in words:
                continue
            else:
                tar = stack.pop()
                if tar == '{' and i != '}':
                    return 0
                if tar == '[' and i != ']':
                    return 0
                if tar == '(' and i != ')':
                    return 0
    except:
        return 0
    if stack:
        return 0
    else:
        return 1
solution(S)


