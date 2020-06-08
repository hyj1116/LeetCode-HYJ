import random
from collections import defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        ave = len(s) // 4  # 在Balanced String中平均每個字元應該有幾個
        d = defaultdict(int)
        res = 0
        for ch in s:
            d[ch] += 1
        for ch in 'QWER':
            if ch not in d:
                d[ch] == 0
        print(d)
        for v in d.values():
            if v < ave:
                res += ave - v
        return res


if __name__ == "__main__":
    solution = Solution()
    my_list = "WWEQERQWQWWRWWERQWEQ"
    li = list(my_list)
    li.sort()
    print(li)
    print(solution.balancedString(my_list))
