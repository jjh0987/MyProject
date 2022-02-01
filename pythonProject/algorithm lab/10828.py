import sys
temp = []
for i in range(int(input())):
    state = sys.stdin.readline()
    if len(state) > 6:
        state = state.split()
        temp.append(int(state[1]))
    elif state == 'pop\n':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp.pop(-1))
    elif state == 'size\n':
        print(len(temp))
    elif state == 'empty\n':
        if len(temp) == 0:
            print(1)
        else:
            print(0)
    elif state == 'top\n':
        if len(temp) == 0:
            print(-1)
        else:
            print(temp[-1])