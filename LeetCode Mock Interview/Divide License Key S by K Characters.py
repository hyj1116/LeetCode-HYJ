class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        1. Make all characters uppercase.
        2. Divide S by K into G groups which G is ceil(S//2)
        3. The first group has len(S) - G*S
        4. Concatenate the G groups with '-'
        """
        S = S.upper()
        if len(S) % K == 0:
            groups = len(S) // K
            first_group_len = K
        else:
            groups = len(S) // K + 1
            first_group_len = len(S) - (groups - 1) * K
        res = [S[:first_group_len]]
        for i in range(groups - 1):
            res.append(S[first_group_len + i * K : first_group_len + (i + 1) * K])

        res = "-".join(res)
        return res


sol = Solution()
S = "5F3Z-2e-9-w"
print(sol.licenseKeyFormatting(S, 4))
