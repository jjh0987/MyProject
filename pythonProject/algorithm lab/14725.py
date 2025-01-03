import sys
input = sys.stdin.readline

n = int(input())
trie = {}
for _ in range(n):
    words = input().rstrip('\n').split()[1:]
    node = trie
    for word in words:
        if word not in node:
            node[word] = {}
        node = node[word]
    node['$'] = True



    node = trie
    stack = []
    for word in sorted(node,reverse=True):
        print(i)


trie