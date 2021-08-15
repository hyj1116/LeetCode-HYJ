import random
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            if points[i][0] == points[i-1][0]:
                res += abs(points[i][1] - points[i-1][1])
            elif points[i][1] == points[i-1][1]:
                res += abs(points[i][0] - points[i-1][0])
            else:
                res += min(abs(points[i][1]-points[i-1][1]),
                           abs(points[i][0]-points[i-1][0]))
                res += abs(abs(points[i][1]-points[i-1][1]) -
                           abs(points[i][0]-points[i-1][0]))
        return res


if __name__ == "__main__":
    solution = Solution()
    points = [[3, 2], [-2, 2]]
    print(solution.minTimeToVisitAllPoints(points))
