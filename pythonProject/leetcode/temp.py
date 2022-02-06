class Solution(object):
    def mergeKLists(self, lists):
        while len(lists) != 1:
            i = 0
            while i < len(lists)//2:
                lists[i] = Solution().TwoListMerge(lists[2*i],lists[2*i+1])
                i += 1
            for x in range(len(lists)//2):
                if len(lists[2*x+1]) == 0:
                    lists.pop(2*x+1)

        return lists[0]

    def TwoListMerge(self,list1,list2):
        merge = []
        while 1:
            try:
                if list1[0] <= list2[0]:
                    merge.append(list1.pop(0))
                else:
                    merge.append(list2.pop(0))
            except:
                break
        for _ in range(len(list1)):
            merge.append(list1.pop(0))
        for _ in range(len(list2)):
            merge.append(list2.pop(0))
        return merge


Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]])


class Solution(object):
    def mergeKLists(self, lists):
        while len(lists) != 1:
            i = 0
            while i < len(lists)//2:
                lists[i] = Solution().TwoListMerge(lists[2*i],lists[2*i+1])
                i += 1
            for x in range(len(lists)//2):
                if len(lists[2*x+1]) == 0:
                    lists.pop(2*x+1)

        return lists[0]

    def TwoListMerge(self,list1,list2):
        merge = []
        while 1:
            try:
                if list1[0] <= list2[0]:
                    merge.append(list1.pop(0))
                else:
                    merge.append(list2.pop(0))
            except:
                break
        for _ in range(len(list1)):
            merge.append(list1.pop(0))
        for _ in range(len(list2)):
            merge.append(list2.pop(0))
        return merge