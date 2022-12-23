n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

people = list(range(1,n+1))
cycle = 1
ans = [0,0]
for i in range(1,len(words)):
    if words[i-1][-1] == words[i][0]:
        cycle += 1
    if cycle == n:
        cycle = 0
        ans[1] += 1


# [num,cycle]