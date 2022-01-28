class Solution(object):
    def twoSum(self, nums, target):
        s_nums = nums
        ans = []
        k = -1
        for j in range(len(s_nums)-1,0,-1):
            for i in range(len(s_nums)+k):
                if s_nums[j]+s_nums[i] == target:
                    if s_nums[j] == s_nums[i]:
                        temp = s_nums[i]
                        ans.append(s_nums.index(temp))
                        s_nums.pop(s_nums.index(temp))
                        ans.append(s_nums.index(temp)+1)
                        break
                    ans.append(s_nums.index(s_nums[i]))
                    ans.append(s_nums.index(s_nums[j]))
                    break
            k -= 1
            if len(ans) == 2:
                break
        return ans

# use hash value
class Solution(object):
    def twoSum(self, nums, target):
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if ((target-num) in table) and (i != table[(target-num)]):
                return [i, table[(target-num)]]