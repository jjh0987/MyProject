temperature = 28 # inside cal_temp
ini_temp = temperature
t1 = 18
t2 = 26
a = 10
b = 8
onboard = [0, 0, 1, 1, 1, 1, 1, 0]

inside = {i for i in range(t1,t2+1)}
setting_temp = 0
if min(inside) >= temperature:
    setting_temp = min(inside)
elif max(inside) <= temperature:
    setting_temp = max(inside)

import collections
onboard = collections.deque(onboard)
cnt = 0
zero_timer = []
for i in range(len(onboard)):
    tar = onboard.popleft()
    if tar == 0:
        cnt += 1
        onboard.append(tar)
        if i == len(onboard):
            zero_timer.append(cnt)
    else:
        zero_timer.append(cnt)
        cnt = 0
        onboard.append(tar)

while onboard:
    tar = onboard.popleft()
