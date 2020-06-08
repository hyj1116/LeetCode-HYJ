import random
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int):
        res = []
        if customfunction == 1:
            for i in range(1, z):
                res.append([i, z-i])
        elif customfunction == 2:
            for i in range(1, z+1):
                if z % i == 0:
                    res.append([i, z//i])
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSolution(2, 5))
