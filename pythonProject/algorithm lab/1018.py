import sys

input = sys.stdin.readline
n,m = map(int,input().split())
target = [input() for _ in range(n)]
target = [list(i.rstrip('\n')) for i in target]

# target = '''BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# BBBBBBBBWBWBW
# BBBBBBBBBWBWB
# WWWWWWWWWWBWB
# WWWWWWWWWWBWB'''
# target = [list(i) for i in target.split()]

answer_case = ['''BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB''',
               '''WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW''']
answer_case = [[list(j) for j in i.split('\n')] for i in answer_case]
def find_error(target,case):
    ans = 0
    for i in range(8):
        for j in range(8):
            if answer_case[case][i][j] != target[i][j]:
                ans += 1
    return ans

tar_list = []
for dx in range(len(target) - 7):
    for dy in range(len(target[0]) - 7):
        tar = [i[0 + dx:8 + dx] for i in target[0 + dy:8 + dy]]
        tar_list.append(tar)

print(min([min(find_error(i,0),find_error(i,1)) for i in tar_list]))
