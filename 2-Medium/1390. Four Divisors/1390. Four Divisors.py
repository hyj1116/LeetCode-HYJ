import math


class Solution:
    def sumFourDivisors(self, nums):
        res = 0
        for i in nums:
            count = 0
            divisors = []
            for j in range(1, int(math.ceil(math.sqrt(i)))):
                if i % j == 0:
                    divisors.append(j)
                    if j != i // j:
                        divisors.append(i // j)
                        count += 2
                    else:
                        count += 1
            if int((math.sqrt(i))) == math.sqrt(i):
                count += 1
                divisors.append(int(math.ceil(math.sqrt(i))))
            if count == 4:
                for k in divisors:
                    res += k
        return res
        

if __name__ == "__main__":
    solution = Solution()
    nums = [21, 4, 7]
    print(solution.sumFourDivisors(nums))
