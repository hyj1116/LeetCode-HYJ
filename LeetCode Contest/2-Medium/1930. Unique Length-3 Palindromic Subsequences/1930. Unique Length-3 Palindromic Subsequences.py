"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/1330178/Python-Straight-Forward-Solution
"""
import string
class Solution:
    def countPalindromicSubsequence(self, s):
        res = 0

        for c in string.ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res

    def countPalindromicSubsequence(self, s: str) -> int:
            return sum([len(set(s[s.index(c)+1:s.rindex(c)])) for c in set(s)])

if __name__ == '__main__':
    sol=Solution()
    s = "aabca"
    print(sol.countPalindromicSubsequence(s))
