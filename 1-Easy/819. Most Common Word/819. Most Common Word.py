import collections
import re


class Solution:
    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    sol = Solution()
    print(sol.mostCommonWord(paragraph, banned))
