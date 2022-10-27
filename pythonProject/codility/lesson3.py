X = 10
Y = 70
D = 30
a,b = divmod((Y-X),D)

if b > 0:
    a += 1

a
A = [2,3,1,5]
conf = {i: 0 for i in range(1, len(A) + 2)}
for i in range(len(A)):
    conf[A[i]] += 1

for i in conf.keys():
    if conf[i] == 0:
        ans = i
        break

print(ans)


A = [3,1,2,4,3]

tar = [0]*(len(A)-1)

init_tapeA = A[0]
init_tapeB = sum(A[1:])
tar[0] = abs(init_tapeA-init_tapeB)

for i in range(1,len(A)):
    try:
        init_tapeA += A[i]
        init_tapeB -= A[i]
        tar[i] = abs(init_tapeA-init_tapeB)
    except:pass

