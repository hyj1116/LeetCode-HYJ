class Solution:
    def checkStraightLine(self, coordinates):
        m = 0
        # coordinates contains no duplicate point, so we don't need to consider the same points.
        for i in range(1, len(coordinates)):
            if coordinates[i][0] == coordinates[i-1][0]:
                m = float('inf')
            elif coordinates[i][1] == coordinates[i-1][1]:
                m = 0
            else:
                m = (coordinates[i][1] - coordinates[i-1][1]) / \
                    (coordinates[i][0] - coordinates[i-1][0])
            if 'former_m' in dir():
                if former_m != m:
                    return False
            else:
                former_m = m
        return True
        # for i in range(2, len(coordinates)):
        #     if m == float('inf'):
        #         if coordinates[i][0] != coordinates[i-1][0]:
        #             return False
        #     elif m == 0:
        #         if coordinates[i][1] != coordinates[i-1][1]:
        #             return False
        #     else:
        #         if (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) != m:
        #             return False
        # return True


if __name__ == "__main__":
    solution = Solution()
    coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(solution.checkStraightLine(coordinates))
