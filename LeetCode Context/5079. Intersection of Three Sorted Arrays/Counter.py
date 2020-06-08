
import random
from collections import Counter


class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        if (not arr1) or (not arr2) or (not arr3):
            return None
        tmp = []
        for i in arr1:
            tmp.append(str(i))
        for i in arr2:
            tmp.append(str(i))
        for i in arr3:
            tmp.append(str(i))
        c = Counter("".join(tmp))
        res = []
        # 非正解
        for k in c:
            if c[k] == 3:
                tmp.append(int(k))
        res.sort()

        return res


if __name__ == "__main__":
    solution = Solution()
    a = [197, 418, 523, 876, 1356]
    b = [501, 880, 1593, 1710, 1870]
    c = [521, 682, 1337, 1395, 1764]
print(solution.arraysIntersection(a, b, c))
