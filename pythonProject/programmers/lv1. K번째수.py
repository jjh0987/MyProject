array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
ans = []
for command in commands:
    tp = sorted(array[command[0]-1:command[1]])
    ans.append(tp[command[2]-1])