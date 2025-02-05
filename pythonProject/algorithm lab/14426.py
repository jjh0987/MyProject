import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trie = {}
for _ in range(n):
    word = input().rstrip('\n')
    node = trie
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]

answer = 0
for _ in range(m):
    word = input().rstrip('\n')
    node = trie
    cnt = len(word)
    for char in word:
        if char in node:
            node = node[char]
            cnt -= 1
        else:
            break
    if cnt == 0:
        answer += 1
print(answer)