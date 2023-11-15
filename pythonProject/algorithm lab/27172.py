import sys
input = sys.stdin.readline
n = int(input())
target = list(map(int,input().split()))
target.sort()

import tqdm
n = len(range(1,1000000))
target = [i for i in range(1,1000000)]
answer = {target[i]:0 for i in range(n)}
for i in tqdm.tqdm(range(n)):
    for j in range(i+1,n):
        if target[j]%target[i] == 0:
            answer[target[j]] += 1

import concurrent.futures
import sympy

def factorize_large_number(n):
    factors = list(sympy.factorint(n))
    # print(f"숫자 {n}의 소인수: {factors}")

# 대상 숫자 목록
numbers_to_factorize = [i+500000 for i in range(100000)]

# 병렬 처리를 통한 소인수분해
import time
s = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(factorize_large_number, numbers_to_factorize)
e = time.time()
print(e-s)