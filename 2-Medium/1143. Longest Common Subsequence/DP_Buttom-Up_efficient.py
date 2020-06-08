# https://www.youtube.com/watch?v=DuikFLPt8WQ&list=PLSIpQf0NbcClDpWE58Y-oSJro_W3LO8Nb
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = [0]*(m+1)
        temp = 0
        for i in range(n):
            prev = 0
            for j in range(m):
                temp = memo[j+1]
                if text1[i] == text2[j]:
                    memo[j+1] = prev + 1
                else:
                    memo[j+1] = max(memo[j+1], memo[j])
                prev = temp
        return memo[-1]


if __name__ == "__main__":
    solution = Solution()
    text1 = "12345"
    text2 = "12"
    print(solution.longestCommonSubsequence(text1, text2))
