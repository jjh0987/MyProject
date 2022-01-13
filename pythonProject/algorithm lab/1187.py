N = int(input()) # N = 2**K 1 <= K <= 10
arr = list(map(int,input().split())) # 1-1000 사이의 수 2N-1 개
# maximum arr length : 2047 -> extract : 1024 -> sum(extract)%N == 0
dp_count = [0]*1000
for i in arr:
    dp_count[i-1] += 1