storey = 5555

storey = [int(i) for i in ' '.join(str(storey)).split()]
i = len(storey)-1
ans = 0
while i >= 0:
    if i == 0:
        ans += storey[i]
        break

    choice1 = storey[i]+storey[i-1]
    choice2 = (10-storey[i])+(storey[i-1]+1)
    if choice1 == min(choice1,choice2):
        ans += storey[i]
    else:
        ans += 10-storey[i]
        storey[i-1] += 1
    i -= 1