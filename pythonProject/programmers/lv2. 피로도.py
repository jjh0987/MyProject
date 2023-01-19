k = 80
dungeons = [[80,20],[50,40],[30,10]]

# k = 40
# dungeons = [[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]

ans = 0
for dungeon in dungeons:
    dungeon.append(k-dungeon[1])
    dungeon.append(dungeon[0]-dungeon[1])

dungeons.sort(key=lambda x:(-x[2],-x[3]))
for dungeon in dungeons:
    if dungeon[0] <= k:
        k -= dungeon[1]
        ans += 1