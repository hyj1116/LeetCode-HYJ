class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre = list(strs[0])
        for i in range(1, len(strs)):
            try:
                while strs[i].index(strs[0]) != 0:
                    pass
            except ValueError:
                pre.pop()  # 程式到這邊後，應該要接著比對strs[i]，但是現在的寫法會接著處理下個字串strs[i+1]
                if len(pre) == 0:
                    return ""
        return "".join(pre)


sol = Solution()
my_list = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(my_list))
