class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        res = []
        for index in range(len(nums)):
            dic[index] = nums[index]
        dic_items = sorted(dic.items())
        nums.sort()
        dic[0] = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dic[i] = dic[i-1] + 1
            else:
                dic[i] = dic[i-1]
        for i in range(len(nums)):
            res[i] = dic_items[i][1]
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [8, 1, 2, 2, 3]
    print(solution.smallerNumbersThanCurrent(nums))
