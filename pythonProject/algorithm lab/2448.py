n = int(input())


'  *  '
' * * '
'*****'

# def blank_triangle()
def make_tri_head():
    ans = ['  *  ',' * * ','*****']
    return ans

def blank_tri():
    ans = ['     ','     ','     ']
    return ans
# def blank_rev_tri():
#     ans = ['     ','   ',' ']
#     return ans

def str_sum(slist):
    ans = ''
    for s in range(len(slist)):
        if s == 0:
            ans += ' '*3*(n//3-len(slist)) + slist[s]
        else:
            ans += ' ' + slist[s]
    return ans

n = 3
# print(*make_tri_head(),sep='\n')
# print(*[make_tri_head()[i]+' '+make_tri_head()[i] for i in range(3)],sep='\n')

answer = [make_tri_head()]
# for k in range(2,n//3+1):
#     answer.append(list(answer[0]*k))

# for i in range(len(answer)):
#     tp = [[],[],[]]
#     for j in range(len(answer[i])):
#         check = j%3
#         if check == 0:
#             tp[0].append(answer[i][j])
#         elif check == 1:
#             tp[1].append(answer[i][j])
#         elif check == 2:
#             tp[2].append(answer[i][j])
#     answer[i] = tp
#     print(*[str_sum(i) for i in tp],sep='\n')

answer

n = int(input())
import math
iter = int(math.log2(n//3))
import collections
answer = collections.deque([['  *  ', ' * * ', '*****']])
tar = answer.popleft()
while iter > 0:
    tar.extend([i+' '+i for i in tar])
    for i in range(len(tar)):
        tar[i] = tar[i].lstrip()
        tar[i] = tar[i].rstrip()
        tar[i] = ' '*(len(tar)-1-i) + tar[i] + ' '*(len(tar)-1-i)
    iter -= 1
print(*tar,sep='\n')