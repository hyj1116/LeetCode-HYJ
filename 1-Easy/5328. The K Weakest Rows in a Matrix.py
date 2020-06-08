class Solution:
    def kWeakestRows(self, mat, k):
        #         1. Store the index, amount of zeros into a dict
        #         2. Sort the dict by value descending, if the value is the same, sort by key descending
        #         3. Store the keys as a list
        #         4. Return the list within the k range
        dic = {}
        res = []
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            dic[i] = count
        dic = {k: v for k, v in sorted(dic.items(), key=lambda item: (item[1], item[0]))}
        for i in dic.keys():
            res.append(i)
            if len(res) == k:
                return res


dic = {7: "g", 12: 'c', 5: "b", 3: "b", 1: "b"}
dic1 = {k: v for k, v in sorted(
    dic.items(), key=lambda item: (item[1], item[0]))}
print(dic1)
if __name__ == "__main__":
    solution = Solution()

    mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [
        1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
    print(solution.kWeakestRows(mat, 3))
