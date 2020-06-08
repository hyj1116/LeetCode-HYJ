class Solution:
    def createTargetArray(self, nums, index):
        res = list()
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1]
    index = [0]
    print(solution.createTargetArray(nums, index))
