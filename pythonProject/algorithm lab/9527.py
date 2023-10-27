# bin(7)
# bin(-~7)
a,b = map(int,input().split())

# two_list = [2**i for i in range(54)]
# marking_a = 0
# marking_b = 0
# for i in range(54):
#     if a - two_list[i] < 0:
#         marking_a = i-1
#         break
# for i in range(54):
#     if b - two_list[i] < 0:
#         marking_b = i-1
#         break

target = {(2**i)-1:i*2**(i-1) for i in range(1,54+1)} # 2**n - 1 -> 1,3,7,15
target
12 - 7 - 3 - 1
target[7] + target[3] + 3 + target[1] + 1*2
bin(a)

1000
1001
1010
1011
1100
