import random


class Solution:
    def shiftGrid(self, grid, k):
        col, nums = len(grid[0]), sum(grid, [])
        k = k % len(nums)
        nums = nums[-k:] + nums[: -k]
        return [nums[i:i+col] for i in range(0, len(nums), col)]


if __name__ == "__main__":
    solution = Solution()
    grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
    k = 4
    print(solution.shiftGrid(grid, k))
