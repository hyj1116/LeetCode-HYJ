import random
from collections import deque

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        move = k % (len(grid) * len(grid[0]))
        res = deque()
        for i in grid:
            for j in i:
                res.append(j)
        res.rotate(move)
        print(res)
        col = len(grid[0])
        for i in range(len(res)):
            grid[i//col][i % col] = res[i]
        return grid


if __name__ == "__main__":
    solution = Solution()
    grid = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    k = 3
    # Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
    print(solution.shiftGrid(grid, 3))
