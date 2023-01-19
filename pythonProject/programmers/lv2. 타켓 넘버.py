numbers = [1, 1, 1, 1, 1]
target = 3

tar = [0]
for i in numbers:
    temp = []
    for j in tar:
        temp.append(j-i)
        temp.append(j+i)
    tar = temp

tar.count(target)