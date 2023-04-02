babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]

tar = ["aya", "ye", "woo", "ma"]
answer = []
for string in babbling:
    for i in tar:
        string = string.replace(i,'*')
    answer.append(string)

ans = 0
for i in answer:
    if sorted(list(set(i)))[0] == '*' and len(set(i)) == 1:
        ans += 1

