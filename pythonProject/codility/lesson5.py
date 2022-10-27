# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A = [str(i) for i in A]
    tar = ''.join(A).lstrip('1').rstrip('0').split('0')

    ans = 0
    for i in range(len(tar)):
        ans += i * len(tar[i])

    if ans > 1000000000:
        return -1
    else:
        return ans
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    tar_a = divmod(A, K)[1]
    tar_b = divmod(B, K)[1]
    if tar_a > 0:
        if A < K:
            A = K
        else:
            A = A + divmod(A, K)[1]
    if tar_b > 0:
        B = B - divmod(B, K)[1]

    return (B - A) // K + 1

A = 11
B = 345
K = 17

A = 2
B = 7
K = 3
tar_a = divmod(A,K)[1]
tar_b = divmod(B,K)[1]
if tar_a > 0:
    if A < K:
        A = K
    else:
        A = A + divmod(A,K)[1]
if tar_b > 0:
    B = B - divmod(B,K)[1]

(B-A)//K + 1

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]


nucle = ['A','C','G','T']
ans = []
def solution(S, P, Q):
    target = [set(S[P[i]:Q[i]+1]) for i in range(len(P))]
    ans = []
    for i in range(len(P)):
        if 'A' in target[i]:
            ans.append(1)
        elif 'C' in target[i]:
            ans.append(2)
        elif 'G' in target[i]:
            ans.append(3)
        elif 'T' in target[i]:
            ans.append(4)
    return ans

set(S[P[0]:Q[0]+1])

A = [4,2,2,5,1,5,8]
ans = []
for i in range(len(A)-2):
    tar = min((A[i+1]+A[i])/2,(A[i+2]+A[i]+A[i+1])/3)
    ans.append(tar)
ans.append((A[-1]+A[-2])/2)
ans
ans.index(min(ans))