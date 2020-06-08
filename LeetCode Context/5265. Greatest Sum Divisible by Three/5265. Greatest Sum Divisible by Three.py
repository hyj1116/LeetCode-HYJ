import random


class Solution:
    def maxSumDivThree(self, nums):
        nums.sort(reverse=True)
        res, arr0, arr1, arr2 = 0, [], [], []
        for i in nums:
            if i % 3 == 0:
                arr0.append(i)
            elif i % 3 == 1:
                arr1.append(i)
            else:
                arr2.append(i)
        max_len = max(len(arr1), len(arr2))
        min_len = min(len(arr1), len(arr2))
        for i in arr0:
            res += i
        for i in range(0, min_len):
            res += arr1[i]
            res += arr2[i]
        remain_len = max_len - min_len
        if len(arr1) > len(arr2):
            for i in range(min_len, (max_len - (remain_len % 3))):
                res += arr1[i]
        if len(arr2) > len(arr1):
            for i in range(min_len, (max_len - (remain_len % 3))):
                res += arr2[i]

        return res


if __name__ == "__main__":
    solution = Solution()
    my_list = [1, 2, 3, 4, 4]
    print(solution.maxSumDivThree(my_list))
