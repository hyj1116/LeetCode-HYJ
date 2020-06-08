# https://leetcode.com/problems/longest-common-subsequence/
import functools


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @functools.lru_cache(None)
        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return helper(i+1, j+1)+1
            return max(helper(i+1, j), helper(i, j+1))
        return helper(0, 0)

        # @functools.lru_cache(None)
        # def helper(i,j):
        #     if i<0 or j<0:
        #         return 0
        #     if text1[i]==text2[j]:
        #         return helper(i-1,j-1)+1
        #     return max(helper(i-1,j),helper(i,j-1))
        # return helper(len(text1)-1,len(text2)-1)


if __name__ == "__main__":
    solution = Solution()
    text1 = "oxcpqrsvwf"
    text2 = "shmtulqrypy"
    print(solution.longestCommonSubsequence(text1, text2))
