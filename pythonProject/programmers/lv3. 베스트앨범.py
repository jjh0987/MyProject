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