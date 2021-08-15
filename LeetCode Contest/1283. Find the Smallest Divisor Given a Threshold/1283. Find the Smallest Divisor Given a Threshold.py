

class Solution:
    def smallestDivisor(self, nums, threshold):
        res = []
        for divisor in range(1, threshold+1):
            sum = 0
            for num in nums:
                if num // divisor == 0:
                    quotient = 1
                elif num % divisor == 0:
                    quotient = num // divisor
                else:
                    quotient = (num // divisor) + 1
                sum += quotient
            res.append(sum)
        for i in range(0, len(res)-1):
            if res[0] <= threshold:
                return i+1
            if res[i] > threshold and res[i+1] <= threshold:
                return (i+1)+1


if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,5,7,11]
    threshold = 11
    print(solution.smallestDivisor(nums, threshold))
