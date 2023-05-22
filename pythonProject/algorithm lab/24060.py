import sys

n, k = map(int, input().split())
input = sys.stdin.readline
A = list(map(int, input().split()))

step = 0
def merge_sort(A):
    global step
    if len(A) == 1:
        return A

    q = (len(A)+1) // 2
    tmp = []
    L = merge_sort(A[:q])
    R = merge_sort(A[q:])
    i, j = 0, 0
    while (i < len(L)) and (j < len(R)):
        if step == k:
            tmp.extend(L)
            tmp.extend(R)
            return tmp
        if L[i] < R[j]:
            tmp.append(L[i])
            ans.append(L[i])
            i += 1
        else:
            tmp.append(R[j])
            ans.append(R[j])
            j += 1
        step += 1

    while i < len(L):
        tmp.append(L[i])
        ans.append(L[i])
        i += 1
        step += 1

    while j < len(R):
        tmp.append(R[j])
        ans.append(R[j])
        j += 1
        step += 1

    return tmp

ans = merge_sort(A)
if step <= k:
    print(*ans)
else:
    print(-1)


try:
    print(ans[k - 1])
except:
    print(-1)




import sys
n, k = map(int, input().split())
input = sys.stdin.readline
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    global k
    tmp = []
    i,j,t = p,q+1,0
    while (i <= q) and (j <= r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            t += 1
            i += 1
        else:
            tmp.append(A[j])
            t += 1
            j += 1
    while i <= q:
        tmp.append(A[i])
        t += 1
        i += 1
    while j <= r:
        tmp.append(A[j])
        t += 1
        j += 1

    i,t = p,0
    while i <= r:
        if k == 0:
            break
        A[i] = tmp[t]
        i += 1
        t += 1
        k -= 1

if k > 0:
    print(-1)
else:
    print(*A)






import sys
n = map(int, input().split())
input = sys.stdin.readline
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    global ans
    tmp = []
    i,j,t = p,q+1,0
    while (i <= q) and (j <= r):
        if A[i] <= A[j]:
            tmp.append(A[i])
            t += 1
            i += 1
        else:
            tmp.append(A[j])
            t += 1
            j += 1
    while i <= q:
        tmp.append(A[i])
        t += 1
        i += 1
    while j <= r:
        tmp.append(A[j])
        t += 1
        j += 1

    i,t = p,0
    while i <= r:
        if A == B:
            ans = 1
        A[i] = tmp[t]
        i += 1
        t += 1

merge_sort(A,0,len(A)-1)
print(ans)