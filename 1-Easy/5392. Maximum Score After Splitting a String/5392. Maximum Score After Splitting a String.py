from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(1, len(s)):
            left_counter = Counter(s[:i])
            left = left_counter['0']
            right_counter = Counter(s[i:])
            right = right_counter['1']
            res = max(res, left+right)
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "011101"
    print(solution.maxScore(s))
