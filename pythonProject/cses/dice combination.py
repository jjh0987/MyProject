n = int(input())
coin = [1,2,3,4,5,6]
def solve(n,coin):
    temp = []
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        for c in coin:
            temp.append(solve(n-c,coin))
        return sum(temp)

print(solve(n,coin))

