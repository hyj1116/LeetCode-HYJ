# 參考自https://leetcode.com/problems/maximal-rectangle/


class Solution:

    sum = 0

    def maximalArea(self, matrix):
        res = []
        # sum = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print(matrix[row][col])
                if matrix[row][col] != 0:
                    res.append(self.dfs(matrix, row, col))
                    self.sum = 0
        print(res)
        return max(res)

    def dfs(self, matrix, row, col):

        if row < 0 or row == len(matrix) or col < 0 or col == len(matrix[row]):
            return
        if matrix[row][col] == 0:
            return
        matrix[row][col] = 0
        self.dfs(matrix, row+1, col)
        self.dfs(matrix, row, col+1)
        self.dfs(matrix, row-1, col)
        self.dfs(matrix, row, col-1)
        self.sum += 1
        return self.sum


if __name__ == "__main__":
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        # ["1", "0", "1", "1", "1"],
        # ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalArea(matrix))
