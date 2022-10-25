import sys
input = sys.stdin.readline
n = int(input())

tar = list(map(int,input().split()))
tp = [0]*n

ans = 0

def merge_sort(start,end):
    global ans

    if end-start < 1: return
    mid = int(start+(end-start)/2)
    merge_sort(start,mid)
    merge_sort(mid+1,end)

    for i in range(start,end+1):
        tp[i] = tar[i]

    k = start
    idx1 = start
    idx2 = mid + 1
    while idx1 <= mid and idx2 <= end:
        if tp[idx1] > tp[idx2]:
            tar[k] = tp[idx2]
            k += 1
            idx2 += 1
            ans += idx2-k
        else:
            tar[k] = tp[idx1]
            k += 1
            idx1 += 1
    while idx1 <= mid:
        tar[k] = tp[idx1]
        k += 1
        idx1 += 1
    while idx2 <= end:
        tar[k] = tp[idx2]
        k += 1
        idx2 += 1

merge_sort(0,n-1)
print(ans)