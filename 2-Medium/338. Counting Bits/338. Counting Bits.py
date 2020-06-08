class Solution:
    def countBits(self, num):
        res = []
        for i in range(num+1):
            s = bin(i).split('b')[-1]
            count = 0
            for j in s:
                if j == '1':
                    count += 1
            res.append(count)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(2))
