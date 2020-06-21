
import re


class Solution:
    def getFolderNames(self, names):
        res = []
        lookup = {}
        suffix = ""
        for i in names:
            if i in lookup:
                k = lookup[i]
                suffix = "("+str(k)+")"
                if i + suffix in lookup:
                    k += 1
                    suffix = "("+str(k)+")"
                lookup[i+suffix] = 1
                lookup[i] = k+1
                res.append(i+suffix)
            else:
                lookup[i] = 1
                res.append(i)
        return res


if __name__ == "__main__":
    sol = Solution()
    # names1 = ["pes", "fifa", "gta", "pes(2019)"]
    # names2 = ["gta", "gta(1)", "gta", "avalon"]
    names3 = ["onepiece", "onepiece(1)",
              "onepiece(2)", "onepiece(3)", "onepiece"]
    names4 = ["wano", "wano", "wano", "wano"]
    names5 = ["kaido", "kaido(1)", "kaido", "kaido(1)"]
    names6 = ["gta", "gta(1)", "gta", "avalon"]
    # print(sol.getFolderNames(names1))
    # print(sol.getFolderNames(names2))
    print(sol.getFolderNames(names3))
    print(sol.getFolderNames(names4))
    print(sol.getFolderNames(names5))
    print(sol.getFolderNames(names6))
