import sys
import copy
input = sys.stdin.readline
n,k = map(int,input().split())
cnt = copy.deepcopy(k)
A = [0]
A.extend(list(map(int,input().split())))
# A = list(map(int,input().split()))
ans = 0
answer = []
def heapify(A,k,n):
    global ans, cnt, answer
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
    # if ans == cnt:
    #     print(*sorted([A[k],A[smaller]]))
    return list(sorted([A[k],A[smaller]]))

def build_min_heap(A,n):
    global ans, cnt, answer
    for i in range(n//2,0,-1):
        ans += 1
        if cnt == ans:
            print(*heapify(A,i,n))
        # printer(x,y)

def heap_sort(A):
    global ans, cnt, answer
    n = len(A)-1
    build_min_heap(A,n)
    for i in range(n,1,-1):
        try:
            A[1],A[i] = A[i],A[1]
            ans += 1
            # if ans == cnt:
            #     print(*sorted([A[1],A[i]]))
            if cnt == ans:
                print(*list(sorted([A[1],A[i]])))
            # printer(A[1],A[i])
            ans += 1
            if cnt == ans:
                print(*heapify(A,1,i-1))
            # printer(x,y)
        except:print(-1)

heap_sort(A)

