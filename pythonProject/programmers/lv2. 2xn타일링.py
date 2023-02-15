n = 60000

tile = [1,2]

i = 2
while i < n:
    tile.append((tile[i-1]+tile[i-2])%1000000007)
    i += 1