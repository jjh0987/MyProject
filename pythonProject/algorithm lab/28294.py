n, a = map(int, input().split())


def pow(n, a):
    if a == 0:
        return 1
    tp = pow(n, a // 2)
    if a % 2 == 0:
        N = tp * tp
    else:
        N = tp * tp * n
    return N % (10 ** 9 + 7)


N = pow(n, a)
ans = ((n - 1) * N) % (10 ** 9 + 7)
ans += (N * (n - 1) ** 2 * (1 - pow(1 - 1 / n, a - 1))) % (10 ** 9 + 7)
ans += (n * pow(n - 1, a)) % (10 ** 9 + 7)
ans = ans % (10 ** 9 + 7)
print(int(ans))