class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        product = 1
        sum = 0
        for i in num:
            product *= int(i)
            sum += int(i)
        return product - sum

from typing import List
if __name__ == "__main__":
    solution = Solution()
    print(solution.subtractProductAndSum(1))
    