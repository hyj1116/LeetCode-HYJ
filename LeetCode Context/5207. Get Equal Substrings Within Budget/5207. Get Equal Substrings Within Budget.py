class Solution:
    def equalSubstring(self, s, t, maxCost):
        """
        DP
        """
        if maxCost == 0:
            return 1
        res = 0
        for i in range(0, len(s)):
            sum = count = 0
            for j in range(i, len(s)):
                diff = abs(ord(s[j]) - ord(t[j]))
                sum += diff
                if sum <= maxCost:
                    count += 1
                else:
                    break
            if count > res:
                res = count
            # res = count if count > res else res
        return res


sol = Solution()
s = "krrgw"
t = "zjxss"
maxCost = 19
print(sol.equalSubstring(s="krrgw", t="zjxss", maxCost=19))

# "krrgw"
# "zjxss"
# 19
# s = "krrgw"
# t = "zjxss"
# s_list = []
# t_list = []
# diff_list = []
# for i in range(len(s)):
#     s_list.append(ord(s[i]))
#     t_list.append(ord(t[i]))
#     diff_list.append(abs(ord(s[i]) - ord(t[i])))

# print(s_list)
# print(t_list)
# print(diff_list) #[15, 8, 6, 12, 4]
