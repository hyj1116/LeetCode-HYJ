from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes):
        sizeToGroup, res = defaultdict(list), []
        for i, size in enumerate(groupSizes):
            sizeToGroup[size].append(i)
            if len(sizeToGroup[size]) == size:
                res.append(sizeToGroup.pop(size))
        return res


if __name__ == "__main__":
    solution = Solution()
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(solution.groupThePeople(groupSizes))
