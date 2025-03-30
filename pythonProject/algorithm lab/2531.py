import sys
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
bob = [int(input()) for i in range(n)]
bob.extend(bob[:k])

answer = 0
for i in range(n):
    tp = set(bob[i:i+k])
    tp.add(c) # 이 번호에 적혀진 초밥이 현재 벨트 위에 없을 경우, 요리사가 새로 만들어 손님에게 제공한다
    answer = max(answer,len(tp))

print(answer)