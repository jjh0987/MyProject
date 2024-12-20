s = list(input())


def is_p(target):
    for i in range(len(target) // 2):
        if target[i] != target[len(target) - (i + 1)]:
            return False
    return True


for i in range(len(s)):
    if is_p(s[i:]):
        p_index = i
        break

for i in s[:p_index]:
    s.append(i)

print(len(s))