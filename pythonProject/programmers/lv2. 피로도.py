k = 80
dungeons = [[80,20],[50,40],[30,10]]

k = 40
dungeons = [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]

ans = 0
for dungeon in dungeons:
    dungeon.append(k-dungeon[1])
    dungeon.append(dungeon[0]-dungeon[1])

dungeons.sort(key=lambda x:(-x[2],-x[3]))
for dungeon in dungeons:
    if dungeon[0] <= k:
        k -= dungeon[1]
        ans += 1








def solution(k, dungeons):
    answer = 0
    current_state = k
    # fatigue 기준 작은순으로 정렬
    dungeons.sort(key=lambda x: (x[1]))

    while True:
        # 입장가능 데이터 선별
        dungeons = [dungeon for dungeon in dungeons if dungeon[0] <= current_state]

        if len(dungeons) != 0:
            # 차이가 큰 친구 찾기
            difference = [threshold - fatigue for threshold, fatigue in dungeons]
            policy = difference.index(max(difference))

            # 차이가 큰 친구 fatigue 값 차감
            get_threshold, get_fatigue = dungeons[policy]
            current_state -= get_fatigue

            # 의사 결정을 한 정보 지우기
            del dungeons[policy]
            answer += 1

        else:
            break
    return answer

solution(k,dungeons)


k = 80
dungeons = [[80,20],[50,40],[30,10]]
import itertools
all_case = list(itertools.permutations(dungeons, len(dungeons)))

cnt = 0
answer = 0
for i in range(len(all_case)):
    cnt = 0
    for j in range(len(dungeons)):
        if k >= all_case[i][j][0]:
            k -= all_case[i][j][1]
            cnt += 1
    if cnt > answer:
        answer = cnt