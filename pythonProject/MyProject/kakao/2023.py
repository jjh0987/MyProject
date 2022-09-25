today = '2022.05.19'
terms = ['A 6','B 12','C 3']
privacies = ['2021.05.02 A','2021.07.01 B','2022.02.19 C','2022.02.20 C']

terms = dict([i.split() for i in terms])

privacies = [i.split() for i in privacies]

today = [int(i) for i in today.split('.')]

priv_terms = [i[1] for i in privacies]
privacies = [i[0].split('.') for i in privacies]
privacies = [[int(j) for j in i] for i in privacies]

priv_transform = [int(terms[i])*28 for i in priv_terms]

checking = []
for i in privacies:
    tp = [0,0,0]
    #for j in range(3):
    tp[0] = (today[0] - i[0])*(12*28)
    tp[1] = (today[1] - i[1])*(28)
    tp[2] = (today[2] - i[2])

    checking.append(sum(tp))

ans = [checking[i] >= priv_transform[i] for i in range(len(checking))]
answer = []
for i in range(1,len(checking)+1):
    if ans[i-1]:
        answer.append(i)


cap = 2
n = 7
deliver = [1,0,3,1,2,0,0]
pickup = [0,0,0,0,0,0,0]

tar = {i:[deliver[i-1],pickup[i-1]] for i in range(n,0,-1)}
ans = 0
i = n

while i > 0:
    capacity = [cap,cap]
    checking = [0,0]
    marking = []
    while i > 0:
        try:
            checking[0] += tar[i][0]
            checking[1] += tar[i][1]
            tar[i] = [0,0]
            tp = [0,0]
            if checking[0] > capacity[0] or checking[1] > capacity[1]:
                tp[0] = checking[0] - capacity[0]
                tp[1] = checking[1] - capacity[1]
                tar[i] = tp
                break
            if checking[0] > 0 or checking[1] > 0:
                marking.append(i)
        except:
            break
        i -= 1
    if marking != []:
        ans += 2*max(marking)

################################
graph = [['' for _ in range(50)] for _ in range(50)]
graph = [['' for _ in range(2)] for _ in range(2)]
graph[0][0] = '1'
graph[0][1] = '1'
graph[1][1] = '1'
def dfs(x,y,color):
    tp = []
    if x < 0 or y < 0 or x >= 2 or y >= 2:
        return False
    if graph[x][y] == '1':
        tp.append((x,y))
        graph[x][y] = True
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True,tp
    return False

dfs(0,0,1)
graph


def dfs(x,y,color):
    # tp = []
    # if x < 0 or y < 0 or x >= 2 or y >= 2:
    #     return False
    try:
        if graph[x][y] == color:
            # tp.append((x,y))
            graph[x][y] = 'EMPTY'
            dfs(x-1,y,color)
            dfs(x,y-1,color)
            dfs(x+1,y,color)
            dfs(x,y+1,color)
            return True
    except:
        return False

def Merge_dfs(x,y,color,trans):
    # tp = []
    # if x < 0 or y < 0 or x >= 2 or y >= 2:
    #     return False
    if graph[x][y] == color:
        # tp.append((x,y))
        graph[x][y] = trans + '.'
        dfs(x-1,y,color)
        dfs(x,y-1,color)
        dfs(x+1,y,color)
        dfs(x,y+1,color)
        return True

    return False
commands = ['UPDATE 1 1 menu','UPDATE 1 2 category',
            'UPDATE 2 1 bibimbap','UPDATE 2 2 korean','UPDATE 2 3 rice'
            ,'UPDATE 3 1 ramyeon','UPDATE 3 2 korean','UPDATE 2 2 noodle'
            ,'UPDATE 3 4 instant','UPDATE 4 1 pasta','UPDATE 4 2 italian'
            ,'UPDATE 4 3 noodle','MERGE 1 2 1 3','MERGE 1 3 1 4'
            ,'UPDATE korean hansik','UPDATE 1 3 group','UNMERGE 1 4'
            ,'PRINT 1 3','PRINT 1 4']
graph = {j:{i:'EMPTY' for i in range(51)} for j in range(51)}

#tp = 'MERGE 1 2 1 3'
ans = []
merge_info = []
for tp in commands:
    command = tp.split()
    if command[0] == 'UPDATE':
        if len(command) == 4:
            graph[int(command[1])][int(command[2])] = command[3]
        else:
            for i in range(1,51):
                for j in range(1,51):
                    if graph[i][j] == command[1]:
                        graph[i][j] = command[2]
    elif command[0] == 'PRINT':
        ans.append(graph[int(command[1])][int(command[2])])

    elif command[0] == 'MERGE':
        idx = [int(i) for i in command[1:]]
        Merge_dfs(idx[2],idx[3],graph[idx[2]][idx[3]],graph[idx[0]][idx[1]])

    elif command[0] == 'UNMERGE':
        idx1,idx2 = int(command[1]), int(command[2])
        check = graph[idx1][idx2]
        dfs(idx1,idx2,graph[idx1][idx2])
        graph[idx1][idx2] = check



ans
graph