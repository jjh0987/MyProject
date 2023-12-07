import sys
import random
input = sys.stdin.readline

def find_n(type,a):
    # A가 a인지 물어보고 flush를 한다.
    # print에 flush 파라미터를 넣으면 된다.
    print(f"? {type}", a, flush=True)

    # 채점기의 답변을 입력받는다.
    resp = int(input())

    if resp == 1:
        return a, resp

    return a,resp
num_list = list(range(1,10001))
random.shuffle(num_list)
for _ in range(1,10001):
    x = num_list.pop()
    a, resp = find_n('A',x)
    if resp == 1:
        break

num_list = list(range(1,10001))
random.shuffle(num_list)
for _ in range(1,10001):
    x = num_list.pop()
    b, resp = find_n('B',x)
    if resp == 1:
        print('!',a+b)
        break
