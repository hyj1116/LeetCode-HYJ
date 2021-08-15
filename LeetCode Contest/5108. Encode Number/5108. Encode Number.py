import random


class Solution:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        n = 0
        while 2**n - 1 <= num:
            n += 1
        n -= 1
        start = 2**n
        diff = num - start
        res = bin(1+diff)[2:]
        if len(res) < n:
            res = "0"*(n-len(res))+res
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.encode(0))
