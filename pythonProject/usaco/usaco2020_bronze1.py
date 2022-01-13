N,K = map(int,input().split())
lis = input().split()

i = 0
templ = 0
temp = []
temps = ''
while i < N:
    templ += len(lis[i])
    if templ > K:
        for x in temp:
            temps += x+' '
        print(temps)
        temps = ''
        templ = 0
        temp = []
    else:
        temp.append(lis[i])
        i += 1
if len(temp) != 0:
    for x in temp:
        temps += x + ' '
    print(temps)