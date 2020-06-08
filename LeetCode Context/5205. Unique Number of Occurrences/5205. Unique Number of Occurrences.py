from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr):
        c = Counter(arr)
        d = c.values()
        l = list(d)
        print(l)
        print(len(l))
        # l.index(1)
        ha = {}
        for i in l:
        # for i in range(len(l) - 1):
            # if l[i] == l[i + 1]:
            if i in ha:
                return False
            else:
                ha[i] = i

        return True


arr = [1, 1, 2, 1, 5, 3, 7, 2, 9]
sol = Solution()
print(sol.uniqueOccurrences(arr))
