class Solution:
    def minimumMoves(self, s: str) -> int:
        count = 0
        if not s.count("X"):
            return 0
        first_X = s.find("X")
        for i in range(first_X, len(s), 3):
            if i < len(s) and s[i:i+3].count('X'):
                count += 1
        return count


sol = Solution()
# s = "XXOXXXOO"
s = "XXXOOXXX"
s = "XXXOOXXOX"
s = "XXXOOXXXO"
s = "XXOXOOXXXO"
s = "XOXXOOXXXO"
res = sol.minimumMoves(s)
print(res)
