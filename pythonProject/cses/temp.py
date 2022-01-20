N,M = map(int,input().split())
A = sorted([int(i) for i in input().split()])
B = [int(i) for i in input().split()]
# 9 3 9 6 6 8 6 2 6 3

ans1 = []
ans2 = []
for c in B:
    left_idx = 0
    right_idx = len(A)-1
    mid_idx = N//2
    ans = -1
    while 1:
        if left_idx == mid_idx:
            if A[right_idx] == c:
                ans += A.pop(right_idx)+1
                break
            elif A[left_idx] <= c:
                if left_idx < 0:
                    break
                else:
                    ans += A.pop(left_idx)+1
                    break
            else:
                break
        if A[mid_idx] > c:
            right_idx = mid_idx
            mid_idx = int((right_idx-mid_idx)/2)
        elif A[mid_idx] < c:
            left_idx = mid_idx
            mid_idx = int((mid_idx-left_idx)/2)
        elif A[mid_idx] == c:
            ans += A.pop(mid_idx)+1
    if ans != -1:
        ans1.append(ans)
    else:
        ans2.append(ans)
ans1.extend(ans2)
for i in ans1:
    print(i)