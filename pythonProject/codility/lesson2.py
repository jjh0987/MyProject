
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(A, K):
    if not A:
        return A

    q = collections.deque(A)
    for _ in range(K):
        q.appendleft(q.pop())

    return list(q)

A = [9,3,9,3,9,7,9]


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    import collections
    tar = collections.Counter(A)
    for i in tar.keys():
        if tar[i] % 2 == 1:
            ans = i
            break

    return ans