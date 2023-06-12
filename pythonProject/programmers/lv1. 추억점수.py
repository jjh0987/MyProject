name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],
         ["may", "kein", "brin", "deny"],
         ["kon", "kain", "may", "coni"]]

score = {i:j for i,j in zip(name,yearning)}
ans = []
for memory in photo:
    tp = 0
    for people in memory:
        try:
            tp += score[people]
        except:pass
    ans.append(tp)