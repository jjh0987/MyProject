import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    words = [input().rstrip('\n') for _ in range(n)]
    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True

    cnt = 0
    for word in words:
        node = trie
        for char in word:
            node = node[char]
        if len(node) == 1:
            cnt += 1

    if cnt == n:
        print('YES')
    else:
        print('NO')






# # 단어 삽입 함수
# def insert(word, trie):
#     node = trie
#     for char in word:
#         if char not in node:
#             node[char] = {}
#         node = node[char]
#     node['$'] = True  # 단어의 끝을 표시
#
# # 단어 탐색 함수
# def search(word, trie):
#     node = trie
#     for char in word:
#         if char not in node:
#             return False
#         node = node[char]
#     return '$' in node
#
# # 접두사 탐색 함수
# def starts_with(prefix, trie):
#     node = trie
#     for char in prefix:
#         if char not in node:
#             return False
#         node = node[char]
#     return True
#
#
# # 사용 예시
# insert("cat", trie)
# insert("car", trie)
# insert("dog", trie)
#
# print(search("cat", trie))  # 출력: True
# print(search("can", trie))  # 출력: False
# print(starts_with("ca", trie))  # 출력: True
# print(starts_with("do", trie))  # 출력: True
# print(starts_with("bat", trie))  # 출력: False
