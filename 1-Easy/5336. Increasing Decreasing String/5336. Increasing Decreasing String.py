# class Solution:
#     def sortString(self, s):
#         s.sort()
#         temp = []
#         res = []
#         for i in s:
#             if i not in temp:
#                 temp.append(i)
#         dic_ = {}
#         for i in s:
#             if i not in dic_:
#                 dic_[i] = 1
#             else:
#                 dic_[i] += 1
#         dic.sort
from collections import Counter


class Solution:
    def sortString(self, s):
        res = ""
        x = Counter(s)
        flag = False
        while len(x.items()):
            items = sorted(x.items(), key=lambda i: i[0], reverse=flag)
            for i in items:
                res += i[0]
                x -= Counter(i[0])
            flag = not flag
            items.reverse()
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "kwgnfmmfngwk"
    print(solution.sortString((s)))
