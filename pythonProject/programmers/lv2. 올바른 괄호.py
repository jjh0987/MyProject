def solution(s):
    stack = []
    for check in s:
        if check == '(':
            stack.append(check)
        else:
            if not stack:
                return False
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False

solution("(()(")