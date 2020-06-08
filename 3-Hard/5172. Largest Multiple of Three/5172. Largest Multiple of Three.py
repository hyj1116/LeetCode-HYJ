class Solution:
    def largestMultipleOfThree(self, digits):
        dic0 = []
        dic1 = []
        dic2 = []
        digits.sort()
        sum = 0
        for i in digits:
            if i % 3 == 1:
                dic1.append(i)
            elif i % 3 == 2:
                dic2.append(i)
            else:
                dic0.append(i)
            sum += i
        if sum % 3 == 1:
            if len(dic1) > 0:
                dic1.sort(reverse=True)
                dic1.pop()
            else:
                dic2.sort(reverse=True)
                dic2.pop()
                dic2.pop()
        elif sum % 3 == 2:
            if len(dic2) > 0:
                dic2.sort(reverse=True)
                dic2.pop()
            else:
                dic1.sort(reverse=True)
                dic1.pop()
                dic1.pop()
        dic0.extend(dic1)
        dic0.extend(dic2)
        dic0.sort()
        res = 0
        if len(dic0) == 0:
            return ""
        else:
            for i in range(len(dic0)):
                res += dic0[i]*(10**i)
            return str(res)


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestMultipleOfThree([2, 1, 1, 1, 1, 2]))
    print(solution.largestMultipleOfThree([2, 1, 1, 1, 1]))
    print(solution.largestMultipleOfThree([2, 1, 1, 1]))
    print(solution.largestMultipleOfThree([1, 1]))
    print(solution.largestMultipleOfThree([8, 7, 6, 1, 0]))
    print(solution.largestMultipleOfThree([1, 1,  2, 2, 2, 2,  2, 2, 2]))
    print(solution.largestMultipleOfThree([2,  1, 1, 1, 1, 1, 1]))
