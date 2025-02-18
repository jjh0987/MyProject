import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))

answers = []
answer = []
tp = [i for i in nums]
for i in range(n):
    j = tp.index(i+1)
    if i != j:
        answer.append((i+1,j+1))
        tp = tp[:i] + list(reversed(tp[i:j+1])) + tp[j+1:]
answers.append(answer)

answer = []
tp = [i for i in nums]
for i in range(n-1,-1,-1):
    j = tp.index(i+1)
    if j != i:
        answer.append((j+1,i+1))
        tp = tp[:j] + list(reversed(tp[j:i+1])) + tp[i+1:]
answers.append(answer)


for answer in answers:
    if not answer:
        print(1,1)
        print(1,1)
        break
    elif len(answer) == 1:
        print(1,1)
        for i in answer:
            print(*i)
        break
    elif len(answer) == 2:
        for i in answer:
            print(*i)
        break

'''
8

1 2 5 6 3 4 7 8

(6 3 4)를 뒤집고 (5 4 3)
'''