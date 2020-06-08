class Solution:
    def getNoZeroIntegers(self, n):
        for n1 in range(1, n//2+1):
            s1 = str(n1)
            r1 = True
            for i in s1:
                if i == '0':
                    r1 = False
                    break

            if r1 == True:
                n2 = n - n1
                s2 = str(n2)
                r2 = True
                for i in s2:
                    if i == '0':
                        r2 = False
                        break
                if r2 == True:
                    return [n1, n2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.getNoZeroIntegers(11))
