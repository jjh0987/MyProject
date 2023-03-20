wallpaper = [".#...", "..#..", "...#."]

file_loc = []
for i in range(len(wallpaper)):
    for j in range(len(wallpaper[0])):
        if wallpaper[i][j] == '#':
            file_loc.append([i,j])

answer = []
answer.extend([min([i[0] for i in file_loc]),min([i[1] for i in file_loc])])
answer.extend([max([i[0] for i in file_loc])+1,max([i[1] for i in file_loc])+1])



