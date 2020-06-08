class Solution:
    def getStrongest(self, arr, k):
        if len(arr) == 1:
            return arr
        res = []
        sorted_arr = sorted(arr)
        mid = sorted_arr[(len(arr)-1)//2]
        print(mid)
        dic = {}
        for i in range(len(arr)):
            dic[i] = abs(arr[i]-mid)
        sorted_values = {k: v for k, v in sorted(
            dic.items(), key=lambda item: [item[1], arr[item[0]]], reverse=True)}
        print(sorted_values)
        for i in sorted_values:
            if len(res) < k:
                res.append(arr[i])
            else:
                return res
        return res

if __name__ == "__main__":
    solution = Solution()
    arr = [-493, 598, -262, -918, -76, -532, 521]
    k = 7
    print(solution.getStrongest(arr, k))
