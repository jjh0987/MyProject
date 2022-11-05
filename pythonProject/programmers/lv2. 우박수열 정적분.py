def solution(k, ranges):
    num = []
    def collatz(x):
        if x == 1:
            num.append(1)
            return
        if x%2 == 0:
            num.append(x)
            collatz(x//2)
        else:
            num.append(x)
            collatz(3*x+1)
    collatz(k)
    square = [(num[i]+num[i+1])/2 for i in range(len(num)-1)]
    ans = []
    for query in ranges:
        a = query[0]
        b = len(num)-1 + query[1]
        if b < a:
            ans.append(-1)
        else:
            ans.append(float(sum(square[a:b])))
    return ans