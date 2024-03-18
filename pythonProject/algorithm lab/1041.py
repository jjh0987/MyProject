import sys
input = sys.stdin.readline

n = int(input())
die = list(map(int,input().split()))
min_die = [min(die[0],die[5]),
            min(die[1],die[4]),
            min(die[2],die[3])]
min_die.sort()
ans = 0
if n == 1:
    ans += sum(sorted(die)[:5])
elif n == 2:
    n1 = 0
    n2 = 4
    n3 = 4
    ans += n2*sum(min_die[:2]) + n3*sum(min_die[:3])
elif n >= 3:
    n1 = 5*(n-2)**2 + 4*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4
    ans += n1*sum(min_die[:1]) + n2*sum(min_die[:2]) + n3*sum(min_die[:3])

print(ans)    