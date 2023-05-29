import sys
input = sys.stdin.readline
n,k = map(int,input().split())
A = [0]
A.extend(list(map(int,input().split())))
# A = list(map(int,input().split()))
ans = 0
def heapify(A,k,n):
    global ans
    left = 2*k
    right = 2*k+1
    if right <= n:
        if A[left] < A[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if A[smaller] < A[k]:
        A[k],A[smaller] = A[smaller],A[k]
        heapify(A,smaller,n)

    print(A[k],A[smaller])
    return A[k],A[smaller]

def build_min_heap(A,n):
    global ans
    for i in range(n//2,0,-1):
        x,y = heapify(A,i,n)
        printer(x,y)
        ans += 1

def heap_sort(A):
    global ans
    n = len(A)-1
    build_min_heap(A,n)
    for i in range(n,1,-1):
        A[1],A[i] = A[i],A[1]
        ans += 1
        printer(A[1],A[i])
        try:
            x,y = heapify(A,1,i-1)
            printer(x,y)
            ans += 1
        except:
            pass

def printer(x,y):
    global ans
    if ans == k-1:
        tp = sorted([x,y])
        print(tp[0],tp[1])

heap_sort(A)

if ans < k:
    print(-1)