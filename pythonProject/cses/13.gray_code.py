i=int(input())
x = 2**(i-1)
list = []
while x <= 2**i-1:
    list.append(format(x, 'b'))
    x += 1
k=0
list2=[]
while k <= len(list)-1:
    new = ''
    t = 0
    while t < i:
        if list[k][t] == '1':
            new += '0'
            t+=1
        else:
            new += '1'
            t+=1
    list2.append(new)
    k+=1
ans = list+list2
for i in ans:
    print(i)