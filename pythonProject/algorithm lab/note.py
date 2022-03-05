n = int(input())
target = input()

nums = [target[i] for i in range(0,n,2)]
operations = [target[i] for i in range(1,n,2)]
nums
operations
'''
nums_idx_0 = [(nums[i],nums[i+1]) for i in range(0,len(nums),2)]
nums_idx_1 = [nums[0]]
for i in range(1,len(nums),2):
    try:
        nums_idx_1.append((nums[i],nums[i+1]))
    except:
        pass
nums_idx_1.append(nums[-1])
'''
import itertools
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

group_nums = [i for i in pairwise(nums)]
pair1 = [group_nums[i] for i in range(0,len(group_nums),2)]
pair2 = [group_nums[i] for i in range(1,len(group_nums),2)]


pair1_sub = [] # start idx 0
pair2_sub = [] # start idx 1
for i in range(len(pair1)+1):
    pair1_sub += list(itertools.combinations(pair1,i))
for i in range(len(pair2)+1):
    pair2_sub += list(itertools.combinations(pair2,i))

pair1_sub
pair2_sub
