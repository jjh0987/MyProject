players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

players_dict = {players[i]:i for i in range(len(players))}
for call in callings:
    players_dict[call] -= 1
    players[players_dict[call]],players[players_dict[call]+1] = players[players_dict[call]+1],players[players_dict[call]]
    players_dict[players[players_dict[call]+1]] += 1