import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dna = input()[:-1]
# A C G T
least = list(map(int,input().split()))
cnt = 0

tar = dna[:m]
S = {'A':tar.count('A'),'C':tar.count('C'),'G':tar.count('G'),'T':tar.count('T')}

flag = 0
if S['A'] < least[0]:
    flag = 1
if S['C'] < least[1]:
    flag = 1
if S['G'] < least[2]:
    flag = 1
if S['T'] < least[3]:
    flag = 1
if flag == 0:
    cnt += 1

for i in range(1,n-m+1):
    S[dna[i-1]] -= 1
    S[dna[i+m-1]] += 1
    if S['A'] < least[0]:
        continue
    if S['C'] < least[1]:
        continue
    if S['G'] < least[2]:
        continue
    if S['T'] < least[3]:
        continue
    cnt += 1

print(cnt)