import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
i = 0
j = n-1
arr.sort()

ans = 3*(10**10)+7
answer = [0,0,0]
while i < j:
    k = i+1
    flag = -1
    while k < j:
        tp = arr[i] + arr[j] + arr[k]
        if tp < 0:
            ans = min(ans,abs(tp))
            if ans >= abs(tp):
                answer[0] = arr[i]
                answer[2] = arr[j]
                answer[1] = arr[k]
            flag = 0
        elif tp > 0:
            ans = min(ans,abs(tp))
            if ans >= abs(tp):
                answer[0] = arr[i]
                answer[2] = arr[j]
                answer[1] = arr[k]
            flag = 1
        else:
            answer[0] = arr[i]
            answer[2] = arr[j]
            answer[1] = arr[k]
            flag = 2
            break
        k += 1
    if flag == 0:
        i += 1
    elif flag == 1:
        j -= 1
    else:
        break
print(*answer)