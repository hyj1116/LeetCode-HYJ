# https: // ithelp.ithome.com.tw/articles/10213258
import random


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


sol = Solution()
l = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(l))
