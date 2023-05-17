import sys

n, k = map(int, input().split())
input = sys.stdin.readline
A = list(map(int, input().split()))
cnt = 0
ans = []


def merge_sort(A):
    global cnt
    if len(A) == 1:
        return A
    q = (len(A)) // 2
    if cnt == k:
        return A
    cnt += 1
    L = merge_sort(A[:q])
    cnt += 1
    R = merge_sort(A[q:])
    cnt += 1
    return merge(L, R)


def merge(L, R):
    tmp = []
    i, j = 0, 0
    while (i < len(L)) and (j < len(R)):
        if L[i] < R[j]:
            tmp.append(L[i])
            ans.append(L[i])
            i += 1
        else:
            tmp.append(R[j])
            ans.append(R[j])
            j += 1

    while i < len(L):
        tmp.append(L[i])
        ans.append(L[i])
        i += 1
    while j < len(R):
        tmp.append(R[j])
        ans.append(R[j])
        j += 1
    return tmp


print(merge_sort(A))
print(cnt)

