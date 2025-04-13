import sys
import math
input = sys.stdin.readline
s = input().rstrip('\n')
if '.' in s:
    if '(' in s:
        s = s.split('(')
        if len(s) == 2:
            s[-1] = s[-1][:-1]

        zero_cnt = len(s[0][s[0].index('.')+1:])
        nine_cnt = len(s[1])
        nums = [[''.join(s[0].split('.')),'1'+'0'*zero_cnt],
                [s[-1],'9'*nine_cnt + '0'*zero_cnt]]
        if nums[0][0] == '0':
            print(f'{nums[1][0]}/{nums[1][1]}')
        else:
            tp = int(nums[0][1])*int(nums[1][1])
            nums[0][0] = int(nums[0][0])*int(nums[1][1])
            nums[1][0] = int(nums[0][1])*int(nums[1][0])
            nums[0][1] = int(tp)
            nums[1][1] = int(tp)
            great = math.gcd(nums[0][0]+nums[1][0],tp)
            upper = (nums[0][0]+nums[1][0])/great
            lower = tp/great
            print(f'{int(upper)}/{int(lower)}')
    else:
        zero_cnt = len(s[s.index('.')+1:])
        nums = [''.join(s.split('.')),'1'+'0'*zero_cnt]
        nums[0],nums[1] = int(nums[0]),int(nums[1])
        great = math.gcd(nums[0],nums[1])
        upper = int(nums[0]/great)
        lower = int(nums[1]/great)
        print(f'{upper}/{lower}')
else:
    print(f'{s}/1')


