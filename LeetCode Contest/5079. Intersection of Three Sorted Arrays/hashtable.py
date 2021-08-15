import random


class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        if (not arr1) or (not arr2) or (not arr3):
            return None
        ha = {}
        res = []
        for i in arr1:
            if i not in ha:
                ha[i] = 1
            else:
                ha[i] += 1
        for i in arr2:
            if i not in ha:
                ha[i] = 1
            else:
                ha[i] += 1
        for i in arr3:
            if i not in ha:
                ha[i] = 1
            else:
                ha[i] += 1
        for i in ha:
            if ha.get(i) == 3:
                res.append(i)
        res.sort()

        return res


if __name__ == "__main__":
    solution = Solution()
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(solution.arraysIntersection(arr1, arr2, arr3))
