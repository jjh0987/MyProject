numbers = [3,30,34,5,9]
# 각 문자열 비교 위함 x*3
str(int(''.join(sorted([str(i) for i in numbers],key=lambda x:x*3,reverse=True))))

sorted(['333','343434','331','334'])