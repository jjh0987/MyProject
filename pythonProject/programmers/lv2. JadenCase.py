s = "3People   unFollowed me"

ans = [s[0].upper()]
flag = 0
for i in range(1,len(s)):
    if s[i-1] != ' ':
        ans.append(s[i].lower())
    else:
        ans.append(s[i].upper())

''.join(ans)

s = s.split()
s = [i.lower() for i in s]
s = [i[0].upper() + i[1:] for i in s]
' '.join(s)