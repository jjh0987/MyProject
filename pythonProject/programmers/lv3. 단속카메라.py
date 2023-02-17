routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

routes.sort(key=lambda x:[x[0],x[1]])
import collections
routes = collections.deque(routes)

answer = 0
while routes:
    tar = routes.popleft()
    while 1:
        try:
            test = routes.popleft()
            if test[0] > tar[1]:
                routes.appendleft(test)
                break
            if tar[0] < test[0]:
                tar[0] = test[0]
            if tar[1] > test[1]:
                tar[1] = test[1]
        except:
            break
    answer += 1

routes