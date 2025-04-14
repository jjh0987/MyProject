import sys
import collections
input = sys.stdin.readline
s = input().rstrip('\n')

nums = collections.deque()
ops = collections.deque()

try:
    tp = ''
    for i in range(len(s)):
        if s[i] in {'+','-','*','/'}:
            nums.append(tp.lstrip('0'))
            tp = ''
            ops.append(s[i])
        else:
            tp += s[i]
    nums.append(int(tp))

    if nums[0] == '':
        nums.popleft()
        nums.appendleft(int(ops.popleft()+nums.popleft()))
except:
    nums.append(int(s))

def final_calculator(l,o,r):
    if o == '+':
        return int(l) + int(r)
    elif o == '-':
        return int(l) - int(r)
    if o == '*':
        return int(l) * int(r)
    if o == '/':
        return int(int(l)/int(r))

if len(ops) == 0:
    print(nums[0])
elif len(ops) == 1:
    print(final_calculator(nums[0],ops[0],nums[1]))
    # print(int(eval(nums[0]+ops[0]+nums[1])))
elif len(ops) == 2:
    answer = collections.deque()
    operation = ''
    ln1, ln2 = nums[0], nums[1]
    rn1, rn2 = nums[2], nums[1]
    lop, rop = ops[0], ops[1]
    ln = final_calculator(ln1,lop,ln2)
    rn = final_calculator(rn2,rop,rn1)
    # ln = ln1 + lop + ln2
    # rn = rn2 + rop + rn1
    # ln = eval(ln)
    # rn = eval(rn)
    if lop in {'*', '/'} and rop in {'*', '/'}:
        if ln >= rn:
            answer.appendleft(int(ln))
            answer.append(rn1)
            operation += rop
        else:
            answer.append(int(rn))
            answer.appendleft(ln1)
            operation += lop
    elif lop in {'+', '-'} and rop in {'+', '-'}:
        if ln >= rn:
            answer.appendleft(int(ln))
            answer.append(rn1)
            operation += rop
        else:
            answer.append(int(rn))
            answer.appendleft(ln1)
            operation += lop
    elif lop in {'*', '/'} and rop in {'+', '-'}:
        answer.appendleft(int(ln))
        answer.append(rn1)
        operation += rop
    else:
        answer.append(int(rn))
        answer.appendleft(ln1)
        operation += lop
    print(final_calculator(answer[0],operation,answer[1]))
    # print(eval(answer[0] + operation + answer[1]))
else:
    def setter():
        if ln >= rn:
            nums.appendleft(int(ln))
            nums.append(rn2)
            nums.append(rn1)
            ops.append(rop)
        else:
            nums.append(int(rn))
            nums.appendleft(ln2)
            nums.appendleft(ln1)
            ops.appendleft(lop)

    while len(ops) > 2:
        ln1, ln2 = nums.popleft(), nums.popleft()
        rn1, rn2 = nums.pop(), nums.pop()
        lop, rop = ops.popleft(), ops.pop()
        ln = final_calculator(ln1, lop, ln2)
        rn = final_calculator(rn2, rop, rn1)
        # ln = ln1 + lop + ln2
        # rn = rn2 + rop + rn1
        # ln = eval(ln)
        # rn = eval(rn)
        if lop in {'*','/'} and rop in {'*','/'}:
            setter()
        elif lop in {'+','-'} and rop in {'+','-'}:
            setter()
        elif lop in {'*','/'} and rop in {'+','-'}:
            nums.appendleft(int(ln))
            nums.append(rn2)
            nums.append(rn1)
            ops.append(rop)
        else:
            nums.append(int(rn))
            nums.appendleft(ln2)
            nums.appendleft(ln1)
            ops.appendleft(lop)

    answer = collections.deque()
    operation = ''
    ln1, ln2 = nums[0], nums[1]
    rn1, rn2 = nums[2], nums[1]
    lop, rop = ops[0], ops[1]
    ln = final_calculator(ln1,lop,ln2)
    rn = final_calculator(rn2,rop,rn1)
    # ln = ln1 + lop + ln2
    # rn = rn2 + rop + rn1
    # ln = eval(ln)
    # rn = eval(rn)
    if lop in {'*', '/'} and rop in {'*', '/'}:
        if ln >= rn:
            answer.appendleft(int(ln))
            answer.append(rn1)
            operation += rop
        else:
            answer.append(int(rn))
            answer.appendleft(ln1)
            operation += lop
    elif lop in {'+', '-'} and rop in {'+', '-'}:
        if ln >= rn:
            answer.appendleft(int(ln))
            answer.append(rn1)
            operation += rop
        else:
            answer.append(int(rn))
            answer.appendleft(ln1)
            operation += lop
    elif lop in {'*', '/'} and rop in {'+', '-'}:
        answer.appendleft(int(ln))
        answer.append(rn1)
        operation += rop
    else:
        answer.append(int(rn))
        answer.appendleft(ln1)
        operation += lop
    print(final_calculator(answer[0],operation,answer[1]))
    # print(eval(answer[0]+operation+answer[1]))