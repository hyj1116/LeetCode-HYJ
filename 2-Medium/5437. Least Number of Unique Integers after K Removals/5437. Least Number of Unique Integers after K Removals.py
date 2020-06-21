class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)
        values = sorted(dic.values(), reverse=True)
        print(values)
        while k > 0:
            k -= values[-1]
            if k >= 0:
                values.pop()
        return len(values)


if __name__ == "__main__":
    solution = Solution()
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    print(solution.findLeastNumOfUniqueInts(arr, k))
