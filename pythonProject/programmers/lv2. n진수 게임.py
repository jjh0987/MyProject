n,t,m,p = 16,16,2,1


maxima = 100000
mapping = {i:str(i) for i in range(10)}
mapping[10] = 'A'
mapping[11] = 'B'
mapping[12] = 'C'
mapping[13] = 'D'
mapping[14] = 'E'
mapping[15] = 'F'

def converter(q,n):
    tar = []
    while q > 0:
        q,r = divmod(q,n)
        tar.append(mapping[r])
    return ''.join(list(reversed(tar)))

target = '0'
i = 1
while len(target) < maxima:
    target += converter(i,n)
    i += 1

ans = ''
i = 0
while i < t:
    ans += target[m*i+p-1]
    i += 1

ans