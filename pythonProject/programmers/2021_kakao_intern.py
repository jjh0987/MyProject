# 1
def solution(s):
    label = {'zero':'0','one':'1','two':'2','three':'3','four':'4',
         'five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    ans = ''
    target = ''
    for i in s:
        target += i
        if target in label:
            ans += label[target]
            target = ''
        else:
            if i.isdigit():
                ans += i
                target = ''
            else:
                pass
    return int(ans)