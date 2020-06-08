class Solution:
    def findAnagrams(self, s, p):
        res = []
        for i in range(len(s)-len(p)+1):
            slist = list(s[i:i+len(p)])
            slist.sort()
            slist = str(slist)
            print(slist)
            plist = list(p)
            plist.sort()
            plist = str(plist)
            if plist in slist:
                res.append(i)
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "abab"
    p = "ab"
    print(solution.findAnagrams(s, p))
