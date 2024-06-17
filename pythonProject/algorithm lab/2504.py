import collections

data = collections.deque(list(input()))
check = {'(', ')', '[', ']'}
data.append(data.popleft())

try:
    for _ in range(1000):
        tar = data.popleft()
        if tar != ')' or tar != ']':
            data.append(tar)

        if data[0] not in check and data[-1] not in check:
            a = int(data.popleft())
            b = int(data.pop())
            data.append(str(a + b))
        elif tar not in check:
            data.pop()
            if data[-1] == '(' and data[0] == ')':
                data.pop()
                data.append(str(int(tar) * 2))
                data.popleft()
            elif data[-1] == '[' and data[0] == ']':
                data.pop()
                data.append(str(int(tar) * 3))
                data.popleft()
            else:
                data.append(tar)
        elif data[-1] == '(' and data[0] == ')':
            data.pop()
            data.popleft()
            data.append('2')
        elif data[-1] == '[' and data[0] == ']':
            data.pop()
            data.popleft()
            data.append('3')

    print(0)
except:
    print(tar)            