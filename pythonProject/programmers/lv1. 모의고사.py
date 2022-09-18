def solution(answers):
    cycle1 = [1,2,3,4,5] * int(10000/5)
    cycle2 = [2,1,2,3,2,4,2,5] * int(10000/8)
    cycle3 = [3,3,1,1,2,2,4,4,5,5] * int(10000/10)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(answers)):
        if cycle1[i] == answers[i]:
            cnt1 += 1
        if cycle2[i] == answers[i]:
            cnt2 += 1
        if cycle3[i] == answers[i]:
            cnt3 += 1

    ans = []
    if max(cnt1,cnt2,cnt3) == cnt1:
        ans.append(1)
    if max(cnt1,cnt2,cnt3) == cnt2:
        ans.append(2)
    if max(cnt1,cnt2,cnt3) == cnt3:
        ans.append(3)
    return ans