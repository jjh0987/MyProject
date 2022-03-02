# 10988
target = input()
if target == target[::-1]:
    print(1)
else:
    print(0)

# 2711
for _ in range(int(input())):
    target = list(map(str,input().split()))
    print(target[1][:int(target[0])-1]+target[1][int(target[0]):])

# 17249
import sys
input = sys.stdin.readline
target = input()
target_sp = target.split('(^0^)')
print(target_sp[0].count('@'),target_sp[1].count('@'))

# 2789
erase = ' '.join('CAMBRIDGE').split()
target = input()
ans = ''
for i in target:
    if i in erase:
        pass
    else:
        ans += i
print(ans)