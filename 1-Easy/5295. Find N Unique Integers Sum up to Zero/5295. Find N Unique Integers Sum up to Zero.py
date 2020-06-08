import math


class Solution:
    def sumZero(self, n):
        if n == 1:
            return [0]

        res = []
        for i in range(-(n-1)//2, math.ceil((n+1)/2)):
            if n % 2 == 0 and i == 0:
                continue
            res.append(i)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumZero(4))
