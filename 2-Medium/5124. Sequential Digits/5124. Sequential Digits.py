import random
from typing import List


class Solution:
    def sequentialDigits(self, low, high):
        num = 0
        len_low = len(low)
        res = []
        for i in range(len(low)-1):
            low = low % 10
        for i in reversed(range(len_low)):
            if low+(len_low-i-1) 
            num += 10**i*(low+(len_low-i-1))            
        if num < high:
            res.append(num)
        
        start = []
        res = []

        for i in low:
            start.append(low[0]+i)
        while start[-1] <= 9:
            num = 0
            for i in start:
                num += start[i]*(10**(len(start)-1-i))
            if num < high:
                res.append(num)
            for i in start:
                start[i] += 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.sequentialDigits(100, 300))
