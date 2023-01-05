arr1 = [[3, 3], [3, 3]]
arr2 = [[1, 4, 3], [2, 4, 1]]


def cross(tp1,tp2):
    ans = 0
    for i in range(len(tp1)):
        ans += tp1[i]*tp2[i]
    return ans


ans = [[0]*len(arr2[0]) for _ in range(len(arr1))]
for j in range(len(arr1)):
    for k in range(len(arr2[0])):
        ans[j][k] = cross(arr1[j],[i[k] for i in arr2])