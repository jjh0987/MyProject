import sys
input = sys.stdin.readline

from decimal import Decimal, ROUND_HALF_UP

def round_decimal(value):
    return float(Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

T = int(input())
for _ in range(T):
    r,b,m = map(float,input().split())
    cnt = 0
    flag = False
    while 1:
        if b > 500000 or cnt > 1200:
            flag = True
            break
        if b <= 0:
            break

        tp = round_decimal(b*(r/100))
        b = round_decimal(b + tp - m)
        cnt += 1
        # print(r,b,m,cnt)
    if flag:
        print('impossible')
    else:
        print(cnt)