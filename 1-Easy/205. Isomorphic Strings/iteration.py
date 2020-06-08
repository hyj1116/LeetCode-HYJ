import random


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return [s.find(i) for i in s] == [t.find(j) for j in t]

        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
            # d1[val] = i
        for i, val in enumerate(t):
            # d2[val] = i
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())


if __name__ == "__main__":
    solution = Solution()
    s = 'abba'
    t = 'abab'
    print(solution.isIsomorphic(s, t))
