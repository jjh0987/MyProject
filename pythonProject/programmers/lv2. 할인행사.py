want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

import collections
collections.Counter(discount)

buy_list = {want[i]:number[i] for i in range(len(want))}

ans = 0
for i in range(len(discount)-9):
    if buy_list == collections.Counter(discount[i:i+10]):
        ans += 1

