
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Linear scan
        """
        chars = list(s)
        start = maximum = 0
        stack = []
        for i in range(len(chars)):
            if chars[i] in stack:
                start = chars.index(chars[i], start, i-1)+1
                maximum = max(maximum, i - start + 1)
            stack.append(chars[i])
        return maximum


if __name__ == "__main__":
    solution = Solution()
    my_list = 'abcabcbb'
    print(solution.lengthOfLongestSubstring(my_list))
    my