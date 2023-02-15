msg = 'KAKAO'

from string import ascii_uppercase
dictionary = list(ascii_uppercase)
dictionary = {dictionary[i]:i+1 for i in range(len(dictionary))}
dictionary[''] = 0

ans = []
i = 0
while i < len(msg):
    w = ''
    while 1:
        if w not in dictionary:
            dictionary[w] = len(dictionary)
            w = w[:-1]
            i -= 1
            break
        try:
            w += msg[i]
        except:break
        i += 1
    if w in dictionary:
        ans.append(dictionary[w])



dictionary