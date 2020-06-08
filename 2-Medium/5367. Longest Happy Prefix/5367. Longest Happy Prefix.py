class Solution:
    def longestPrefix(self, s):
        for i in range(1, len(s)):
            if s.startswith(s[i:]):
                return s[i:]
        return ""


if __name__ == "__main__":
    solution = Solution()
    s = "ababab"
    # s = "aaaaa"
    print(solution.longestPrefix(s))
