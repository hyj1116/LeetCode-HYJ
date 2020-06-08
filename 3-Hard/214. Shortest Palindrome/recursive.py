# https://leetcode.com/problems/shortest-palindrome/discuss/60250/My-recursive-Python-solution


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[j:][::-1] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]
