prices = [1, 2, 3, 2, 3]

ans = []
for i in range(len(prices)):
    tp = 0
    for j in range(i,len(prices)):
        tp += 1
        if prices[i] > prices[j]:
            break
    ans.append(tp)

