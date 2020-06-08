from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

        # Solution 2:
        # d = defaultdict(int)
        # for i in t:
        #     d[i] += 1
        # for i in s:
        #     if i in d:
        #         d[i] -= 1
        # for i in t:
        #     if d[i] != 0:
        #         return i

    # 以下方式不適用於 s='aa', t='a'
    #         set_s = set(s)
    #         set_t = set(t)
    #         res = set_t - set_s
    #         return res.pop()


if __name__ == "__main__":
    solution = Solution()
    s = "abcd"
    t = "abcde"
    print(solution.findTheDifference(s, t))
