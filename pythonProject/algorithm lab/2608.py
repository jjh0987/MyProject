import sys
input = sys.stdin.readline

rome_to_a = {'I': 1, 'II': 2, 'III': 3, 'A': 4, 'V': 5,
             'VI': 6, 'VII': 7, 'VIII': 8, 'B': 9,
             'X': 10, 'XX': 20, 'XXX': 30, 'E': 40, 'L': 50,
             'LX': 60,'LXX':70, 'LXXX': 80, 'F': 90, 'C': 100,
             'CC': 200, 'CCC': 300, 'G': 400, 'D': 500,
             'DC': 600, 'DCC': 700, 'DCCC': 800, 'H': 900,
             'M': 1000, 'MM': 2000, 'MMM': 3000}
a_to_rome = {rome_to_a[i]: i for i in rome_to_a}
replace_target = {'IV':'A','IX':'B','XL':'E','XC':'F',
                  'CD':'G','CM':'H'}
reverse_target = {replace_target[i]:i for i in replace_target}

s1 = input().rstrip('\n')
s2 = input().rstrip('\n')
for i in replace_target:
    s1 = s1.replace(i,replace_target[i])
    s2 = s2.replace(i,replace_target[i])

s1 = sum([rome_to_a[i] for i in list(s1)])
s2 = sum([rome_to_a[i] for i in list(s2)])
answer = s1 + s2
print(answer)

answer = list(str(answer))
tp = []
for i in range(len(answer)-1,-1,-1):
    if answer[i] == '0':
        continue
    tp.append(answer[i] + (len(answer)-1-i) * '0')

for i in range(len(tp)-1,-1,-1):
    tp[i] = a_to_rome[int(tp[i])]
    if tp[i] in reverse_target:
        tp[i] = reverse_target[tp[i]]
    print(tp[i], end='')
