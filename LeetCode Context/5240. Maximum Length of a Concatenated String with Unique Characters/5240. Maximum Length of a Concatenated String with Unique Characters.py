import random
from itertools import combinations
from itertools import combinations


class Solution:
    def maxLength(self, arr):
        maximum = res = 0
        res = self.helper(arr, maximum)
        return res

    # A Python program to print all combinations of given length
    def helper(self, arr, maximum):
        if len(arr) == 1:
            return len(arr[0])
        elif len(arr) == 0:
            return maximum

        # Get all combinations of arr and length 2
        comb = combinations(arr, 2)
        temp = []
        for i in comb:
            # intersected = False
            if set(i[0]) - set(i[1]) == set(i[0]):
                # for j in i[0]:
                # if j in i[1]:
                    # intersected = True
                    # break
                # if intersected == False:
                temp.append(i[0]+i[1])
                maximum = max(maximum, len(i[0]) + len(i[1]))
        return self.helper(temp, maximum)


if __name__ == "__main__":
    solution = Solution()
    arr = ["a", "b", "c", "d", "e", "f", "g", "h",
           "i", "j", "k", "l", "m", "n", "o", "p"]
    print(solution.maxLength(arr))
