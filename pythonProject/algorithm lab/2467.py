import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
i = 0
j = n-1
arr.sort()

ans = 2*(10**10)+7
answer = [0,0]
while i < j:
    tp = arr[i] + arr[j]
    if tp < 0:
        ans = min(ans,abs(tp))
        if ans >= abs(tp):
            answer[0] = arr[i]
            answer[1] = arr[j]
        i += 1
    elif tp > 0:
        ans = min(ans,abs(tp))
        if ans >= abs(tp):
            answer[0] = arr[i]
            answer[1] = arr[j]
        j -= 1
    else:
        answer[0] = arr[i]
        answer[1] = arr[j]
        break
print(*answer)              