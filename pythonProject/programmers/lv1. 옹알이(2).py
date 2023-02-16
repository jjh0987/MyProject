babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]

baby = ["aya", "ye", "woo", "ma"]
baby_confirm = [i*2 for i in baby]

answer = 0
for speak in babbling:
    flag = 0
    for i in baby_confirm:
        if i in speak:
            flag = 1
            break

    if flag == 1:
        continue

    for i in baby:
        if i in speak:
            speak = speak.replace(i,' ')

    speak = speak.replace(' ','')
    if not speak:
        answer += 1

