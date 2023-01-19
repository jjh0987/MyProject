n = 4
left = 7
right = 14

start_col, start_pos = divmod(left,n)
end_col, end_pos = divmod(right,n)

ans = []
for i in range(start_col+1,end_col+2):
    tp = []
    for j in range(1,n+1):
        if j <= i:
            tp.append(i)
        else:
            tp.append(j)
    ans.append(tp)
answer = []
for i in ans:
    answer.extend(i)
answer[start_pos:start_pos+right-left+1]