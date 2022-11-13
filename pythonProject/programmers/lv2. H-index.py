citations = [4,4,4]

tar = sorted(citations,reverse=True)
cnt = 0
for i in range(len(tar)):
    if tar[i] <= cnt:
        print(i)
        break
    cnt += 1