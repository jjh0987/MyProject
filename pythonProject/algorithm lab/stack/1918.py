# 문자스택, 연산자스택 넣은후 뽑기
target = input()

operation = set(['+', '-', '*', '/', '(', ')'])
import string
alpha = set(str(string.ascii_uppercase))

target_oper = []
target_alpha = []

token = []
tp = ''
i = 0
while i < len(target):
    if target[i] == ')':
        tp += target[i]
        token.append(tp)
        tp = ''
        i += 1
    elif target[i] in ['*','/']:
        tp += target[i]
        i += 1
        if target[i] == '(':
            continue
        tp += target[i]
        token.append(tp)
        tp = ''
        i += 1
    else:
        tp += target[i]
        i += 1

token