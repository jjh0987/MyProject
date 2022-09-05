import collections

def solution(nums):
    answer = 0
    if int(len(nums)/2) > len(dict(collections.Counter(nums)).keys()):
        answer += len(dict(collections.Counter(nums)).keys())
    else:
        answer += int(len(nums)/2)

    return answer

def solution(participant, completion):
    answer = ''
    counter = dict(collections.Counter(participant))
    for name in completion:
        counter[name] -= 1

    for name in counter:
        if counter[name] == 1:
            answer += name
            break

    return answer