def solution(genres, plays):
    answer = []

    genres = ["classic", "pop", "classic", "classic", "pop",'zb']
    key = list(set(genres))
    plays = [500, 600, 150, 800, 2500,100]
    tp = dict()
    for k in key:
        tp[k] = 0
    for i in zip(genres,plays):
        tp[i[0]] += i[1]
    tp = [[i[1],i[0]] for i in zip(tp.keys(),tp.values())]
    tp.sort()

    sorted_genres = [i[1] for i in tp]
    sorted_genres.reverse()
    sorted_genres

    temp = dict()
    for i in range(len(genres)):
        temp[sorted_genres[i]] = {genres[i]:plays[i]}

    temp
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
genres_dict = {i:0 for i in genres}
for i in range(len(genres)):
    genres_dict[genres[i]] += plays[i]
genres_rank = []
for i in genres_dict:
    genres_rank.append([i,genres_dict[i]])
genres_rank.sort(key=lambda x:x[1],reverse=True)
genres_rank = [i[0] for i in genres_rank]

target = []
for i in range(len(genres)):
    target.append([genres[i],plays[i],i])

target.sort(key=lambda x:(x[1],x[0]),reverse=True)

genres_ans = {i:[] for i in genres_dict.keys()}
for i in target:
    if len(genres_ans[i[0]]) == 2:
        continue
    genres_ans[i[0]].append(i[2])

answer = []
for i in genres_rank:
    answer.extend(genres_ans[i])