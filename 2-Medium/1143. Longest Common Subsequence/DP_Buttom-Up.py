# https://www.youtube.com/watch?v=DuikFLPt8WQ&list=PLSIpQf0NbcClDpWE58Y-oSJro_W3LO8Nb
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    text1 = "ada"
    text2 = "da"
    print(solution.longestCommonSubsequence(text1, text2))