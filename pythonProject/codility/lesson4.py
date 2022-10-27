A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5
def sol(X,A):
    conf = set()
    for i in range(len(A)):
        conf.add(A[i])
        if len(conf) == X:
            return i
    return -1

sol(5, [1, 3, 1, 4, 2, 3, 5, 4])

def solution(A):
    tar = set()
    for i in A:
        if i <= len(A):
            tar.add(i)
    if len(tar) == len(A):
        return 1
    else:
        return 0


def solution(N, A):
    # write your code in Python 3.8.10
    pass


N = 5
A = [3,4,4,6,1,4,4]

# tar = [0]*N
# maxi = 0
# maxi_list = []
# for i in range(len(A)):
#     if A[i] <= N:
#         try:
#             tar[A[i]-1] += 1
#             maxi = max(maxi, tar[A[i]-1])
#         except:
#             tar[A[i]-1] = 1
#     elif A[i] == N+1:
#         tar = [maxi]*N

N = 1
A = [1]
max_counter = [0]
for i in range(len(A)):
    if A[i] == N+1:
        max_counter.append(i)

if max_counter == [0]:
    tar = [0]*N
    for i in range(len(A)):
        if A[i] <= N:
            try:
                tar[A[i]-1] += 1
            except:
                tar[A[i]-1] = 1

if max_counter:
    counter = []
    import collections
    for i in max_counter:
        try:
            counter.append(collections.Counter(A[max_counter[i]:max_counter[i+1]]))
        except:
            pass

    tar = [sum([max(i.values()) for i in counter])] * N
    for i in range(max_counter[-1]+1,len(A)):
        if A[i] <= N:
            try:
                tar[A[i]-1] += 1
            except:
                tar[A[i]-1] = 1


#
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    import collections
    tar = dict(collections.Counter(A))
    for i in range(1, len(tar) + 1):
        try:
            tar[i]
        except:
            return i
    if i == len(tar):
        return i+1

A = [-1,-3]
solution(A)

import collections
tar = dict(collections.Counter(A))
for i in range(1,len(tar)+1):
    try:
        tar[i]
    except:
        print(i)
if i == len(tar):
    print(i+1)