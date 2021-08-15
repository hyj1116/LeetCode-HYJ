import random
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        if (not arr1) or (not arr2) or (not arr3):
            return None
        s1 = set(arr1)
        s2 = set(arr2)
        s3 = set(arr3)
        res = s1.intersection(s2)
        res = res.intersection(s3)
        res = list(res)
        res.sort()

        return res


if __name__ == "__main__":
    solution = Solution()
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 5, 7, 9]
    arr3 = [1, 3, 4, 5, 8]
    print(solution.arraysIntersection(arr1, arr2, arr3))
