record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

record = [i.split() for i in record]
id_nick = dict()
ans = []
for reco in record:
    if len(reco) == 3:
        condition, ID, nick_name = reco
        id_nick[ID] = nick_name
    else:
        condition, ID = reco

    sent = ''
    if condition == 'Enter':
        sent += f'{ID},님이 들어왔습니다.'
    elif condition == 'Leave':
        sent += f'{ID},님이 나갔습니다.'

    if sent:
        ans.append(sent)


answer = []
for sent in ans:
    front, end = sent.split(',')
    answer.append(f'{id_nick[front]}{end}')
answer