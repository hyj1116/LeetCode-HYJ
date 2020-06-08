# https://www.youtube.com/watch?v=DuikFLPt8WQ&list=PLSIpQf0NbcClDpWE58Y-oSJro_W3LO8Nb
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # dp = [[0]*(m+1) for _ in range(n+1)]
        dp = [[0]*(m+1) for _ in range(n+1)]

        def helper(text1, text2, i, j, dp):
            if i <= 0 or j <= 0:
                return 0

            if dp[i][j]:
                return dp[i][j]

            if text1[i-1] == text2[j-1]:
                return 1+helper(text1, text2, i-1, j-1, dp)
            else:
                dp[i][j] = max(helper(text1, text2, i, j-1, dp),
                               helper(text1, text2, i-1, j, dp))
                return dp[i][j]
        return helper(text1, text2, n, m, dp)


if __name__ == "__main__":
    solution = Solution()
    text1 = "aa"
    text2 = "a"
    print(solution.longestCommonSubsequence(text1, text2))
