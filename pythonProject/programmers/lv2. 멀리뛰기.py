n = 100
target = [n,0]
case = [[n,0]]
while target[0] > 1:
    target[0] -= 2
    target[1] += 1
    case.append(sorted([i for i in target],reverse=True))

def combi(n,r):
    n_fact = list(range(n - r + 1, n + 1))
    n_r_fact = list(range(1, r + 1))
    ans = 1
    cnt = 0
    for i in range(len(n_fact)):
        ans *= n_fact[i]
        ans = ans % 1234567
        for j in range(cnt, len(n_r_fact)):
            if ans % n_r_fact[j] == 0:
                ans = int(ans / n_r_fact[j])
                cnt += 1
                break
    return ans


answer = 0
for i in case:
    answer += combi(i[0]+i[1],i[1])
    if answer > 1234567:
        answer = answer % 1234567

print(answer)