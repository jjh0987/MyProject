import sys
N = int(input())
seq = list(map(int,sys.stdin.readline().split()))
seq.reverse()
ans = [-1]
i = 0
j = 0
while 1:
    try:
        if seq[i+j] > seq[i+j+1]:
            ans.append(seq[i+j])
            j += 1
        elif seq[i+j] <= seq[i+j+1]:
            if seq[i] <= seq[i+j+1]:
                ans.append(-1)
                i = i+j+1
                j = 0
            elif seq[i+j] == seq[i+j+1]:
                ans.append(ans[-1])
                j += 1
            else:
                ans.append(seq[i])
                j += 1
    except:
        break
ans.reverse()
print(*ans)


# 1874 
