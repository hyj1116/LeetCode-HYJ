import math


class Solution:
    def closestDivisors(self, num):
        num1 = num+1
        multiplicand1 = math.floor(math.sqrt(num1))
        while num1 % multiplicand1 != 0:
            multiplicand1 -= 1
        multiplier1 = num1 // multiplicand1
        diff1 = abs(multiplicand1-multiplier1)

        num2 = num+2
        multiplicand2 = math.floor(math.sqrt(num2))
        while num2 % multiplicand2 != 0:
            multiplicand2 -= 1
        multiplier2 = num2 // multiplicand2
        diff2 = abs(multiplicand2-multiplier2)

        if diff1 < diff2:
            return [multiplicand1, multiplier1]
        else:
            return [multiplicand2, multiplier2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.closestDivisors(123))
