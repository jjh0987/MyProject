record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

record = [i.split() for i in record]
data = dict()
for target in record:
    if len(target) == 2:
        continue
    if target[0] != 'Leave':
        data[target[1]] = target[2]

result = []
for target in record:
    if target[0] == 'Enter':
        tar = f'{data[target[1]]}님이 들어왔습니다.'
        result.append(tar)
    elif target[0] == 'Leave':
        tar = f'{data[target[1]]}님이 나갔습니다.'
        result.append(tar)



k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]

seq = []
seq.append([0,k])
i = 1
while k > 1:
    if k%2 == 0:
        k /= 2
        seq.append([i,int(k)])
    else:
        k = int(3*k+1)
        seq.append([i,k])
    i += 1

presum = [0 for _ in range(len(seq))]
for i in range(1,len(seq)):
    presum[i] = presum[i-1] + (seq[i][1]+seq[i-1][1])/2

n = len(seq)-1
answer = []
for a,b in ranges:
    b = n+b
    if a <= b:
        answer.append(presum[b]-presum[a])
    else:
        answer.append(-1.0)
answer