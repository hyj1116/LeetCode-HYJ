import copy


class Solution:
    def minGroups(self, intervals):
        intervals.sort()
        pop_list=[]
        count = 0
        while len(intervals) > 0:
            # start = intervals[0][0]
            end = intervals[0][1]
            count += 1
            # tmp = copy.deepcopy(intervals)
            for i in range(1, len(intervals)):
                if intervals[i][0] > end:
                    # start = intervals[i][0]
                    end = intervals[i][1]
                    pop_list.append(i)
                    # tmp.pop(i)
            for i in pop_list:
                intervals.pop(i)
            intervals.pop(0)
            # tmp.pop(0)
            # intervals = copy.deepcopy(tmp)
        return count


sol = Solution()
res = sol.minGroups([[1, 3], [5, 6], [8, 10], [11, 13]])
print(res)
