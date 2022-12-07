s = "abracadabra"
ans = 0
i = 0
while i < len(s):
    try:
        target = s[i]
        ans1 = 0
        ans2 = 0
        while ans1 >= ans2:
            if s[i] == target:
                ans1 += 1
            else:
                ans2 += 1
            if ans1 == ans2:
                ans += 1
                break
            i += 1
        i += 1
    except:
        ans += 1
