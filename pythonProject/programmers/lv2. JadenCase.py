s = "3People  unFollowed me"

ans = [s[0].upper()]
flag = 0
for i in range(1,len(s)):
    if s[i-1] != ' ':
        ans.append(s[i].lower())
    else:
        ans.append(s[i].upper())

''.join(ans)