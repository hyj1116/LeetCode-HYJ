class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        # if i+1 < len(grid) and i-1 >= 0 and j+1 < len(grid[0]) and j-1 >= 0:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = "0"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


if __name__ == "__main__":
    solution = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(solution.numIslands(grid))
