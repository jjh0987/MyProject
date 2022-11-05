# height = [1,4,2,5,3]
# height = [3,4,5,6,7]
# height = [1,99998,99999]
# height = [3,5,4,2,4,4,6,5]
# height = [5,5,5]
#
#
# tar = max(height)
# ans = [0]*len(height)
# i = 1
#
# cnt = 0
# mark = 0
# for j in range(len(height)):
#     if height[j] >= mark:
#         mark = height[j]
#         cnt += 1
# ans[0] = cnt - 1
#
# for i in range(1,len(height)):
#     if ans[i] == 0:
#         cnt = 0
#         mark = 0
#         for j in range(i,len(height)):
#             if height[j] > mark:
#                 mark = height[j]
#                 cnt += 1
#         if i == 0:
#             ans[i] = cnt - 1
#         else:
#             ans[i] = cnt
#
#     if height[i] == tar:
#         ans[i] = 0
#         continue
#
#     if height[i] > height[i-1]:
#         ans[i] = ans[i-1] - 1
#
#     elif height[i] < height[i-1]:
#         try:
#             if height[i] >= height[i+1]:
#                 ans[i] = ans[i-1] + 2
#             else:
#                 ans[i] = ans[i-1] + 1
#         except:pass
#
#     else:
#         ans[i] = ans[i-1]
#
# sum(ans)

height = [3,5,4,2,4,4,6,5]
stack = []
for i in height:
    if not stack:
        stack.append(i)


projects = [[1,2],[1,3],[1,4],[3,5],[3,6],[4,7]]
projects.sort()


value = [10,11,8,5,9,15,17]

check = [False]*(len(value)+1)
graph = {i:[] for i in range(1,len(value)+1)}
for i in projects:
    # graph[i[0]].append(value[i[0]-1]+value[i[1]-1])
    graph[i[0]].append(i[1])
    # graph[i[1]].append(i[0])

end_node = []
for i in graph:
    if not graph[i]:
        end_node.append(i)

graph
