print(1,1,1,sep='@')
print(1,1,end='@')

# 10955
import sys
input = sys.stdin.readline
n = int(input())

if n == 1:
    print('*')
else:
    for i in range(n):
        if i%2 == 0:
            print(' '.join(['*']*n))
        else:
            print(' '+' '.join(['*']*n))

# 2675
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,s = map(str,input().split())
    n = int(n)
    s = ' '.join(s).split()

    ans = ''
    for i in s:
        ans += i*n
    print(ans)

#2941
s = input()
len_s = len(s)
str_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

ans = 0
for i in str_list:
    ans += str(s).count(i)
print(len_s-ans)

# 8892
t = int(input())
for _ in range(t):
    k = int(input())
    temp = []
    for _ in range(k):
        temp.append(input())
    # 'aaba'[::-1]
    x = 0
    for i in range(k):
        for j in range(k):
            if i != j:
                if temp[i]+temp[j] == (temp[i]+temp[j])[::-1]:
                    ans = temp[i]+temp[j]
                    x += 1
                    break
        if x == 1:
            break
    if x == 0:
        print(0)
    else:
        print(ans)

# 2804

string1,string2 = map(str,input().split())
len_s1 = len(string1)
len_s2 = len(string2)
for i in range(len_s1):
    x = 0
    for j in range(len_s2):
        if string1[i] == string2[j]:
            axis_y = i
            axis_x = j
            x += 1
            break
    if x == 1:
        break

ans = ''
k = 0
m = 0
for i in range(len_s2):
    temp = ''
    for j in range(len_s1):
        if j == axis_y and i == axis_x:
            temp += string2[k]
            m += 1
            k += 1
        elif j == axis_y:
            temp += string2[k]
            k += 1
        else:
            if i == axis_x:
                temp += string1[m]
                m += 1
            else:temp += '.'
    ans += temp + '\n'

print(ans)