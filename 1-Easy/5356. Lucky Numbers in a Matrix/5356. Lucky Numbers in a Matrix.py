
class Solution:
    def luckyNumbers(self, matrix):
        res = []
        for i in range(len(matrix)):
            is_lucky = True
            row_min_value = min(matrix[i])
            row_min_index = matrix[i].index(row_min_value)
            for j in range(len(matrix)):
                if row_min_value < matrix[j][row_min_index]:
                    is_lucky = False
                    break
            if is_lucky:
                res = [row_min_value]
        return res


if __name__ == "__main__":
    solution = Solution()
    matrix = [[7, 8], [11, 2]]
    print(solution.luckyNumbers((matrix)))
