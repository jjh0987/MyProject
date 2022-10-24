m = "ABC"
musiccinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
musiccinfos = [i.split(',') for i in musiccinfos]
musiccinfos = {i[2]:[i[0],i[1],i[3]] for i in musiccinfos}
tar_words = []

import collections
for i in musiccinfos.keys():
    minutes = (int(musiccinfos[i][1][:2]) - int(musiccinfos[i][0][:2]))*60 \
              + int(musiccinfos[i][1][-2:]) - int(musiccinfos[i][0][-2:])
    que = collections.deque(musiccinfos[i][-1])
    length = 0
    target = ''
    while length != minutes:
        tar = que.popleft()
        target += tar
        if tar != '#':
            length += 1
        que.append(tar)
    tar_words.append(target)

ans_list = []
for i in range(len(musiccinfos)):
    if m in tar_words[i]:
        if m+'#' in tar_words[i]:
            tar_words[i] = tar_words[i].replace(m+'#','')
        if m in tar_words[i]:
            ans_list.append(list(musiccinfos.keys())[i])


time_lst = []
if len(ans_list) > 1:
    for i in ans_list:
        minutes = (int(musiccinfos[i][1][:2]) - int(musiccinfos[i][0][:2])) * 60 \
                  + int(musiccinfos[i][1][-2:]) - int(musiccinfos[i][0][-2:])
        time_lst.append(minutes)
    answer = ans_list[time_lst.index(max(time_lst))]
elif not ans_list:
    answer = '(None)'
else:
    answer = ans_list[0]