
import math


class Solution:
    def findOriginalArray(self, changed):
        tmp = []
        res = []
        changed.sort()
        # changed.reverse()
        for i in changed:
            if i == 1:
                tmp.append(i)
            else:
                a = math.ceil(i/2)
                if a in tmp:
                    tmp.remove(a)
                    res.append(a)
                else:
                    tmp.append(i)
        if len(tmp) == 0:
            return res
        else:
            return []

#         [2,1,2,4,2,4]
#         4,4,2,2,2,1
# [0,3,2,4,6,0]
# 0,0,2,3,4,6


# changed = [1, 3]
changed = [0, 3, 2, 4, 6, 0]

sol = Solution()
res = sol.findOriginalArray(changed)
print(res)
