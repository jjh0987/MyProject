

A = [1,5,2,1,4,0]
tar = [[i-A[i],i+A[i]] for i in range(len(A))]
tar.sort(key=lambda x:[x[0],x[1]])
tar
ans = 0
i = 0
for i in range(len(tar)):
    for j in range(i+1,len(tar)):
        if tar[i][1] < tar[j][0]:
            ans += j
            break



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    tar = [[i-A[i],i+A[i]] for i in range(len(A))]
    tar.sort(key=lambda x:[x[0],x[1]])
    ans = 0
    i = 0
    for i in range(len(tar)):
        for j in range(i+1,len(tar)):
            if tar[i][1] >= tar[j][0]:
                ans += 1
            else:
                break


    if ans > 10000000:
        return -1
    return ans


def solution(A):
    disc = []
    for i, v in enumerate(A):
        disc.append((i - v, -1))
        disc.append((i + v, 1))

    disc = sorted(disc)
    t = 0
    r = 0

    for d in disc:
        if d[1] == 1:
            t -= 1
        else:
            r += t
            t += 1

    return r if r <= 10000000 else -1