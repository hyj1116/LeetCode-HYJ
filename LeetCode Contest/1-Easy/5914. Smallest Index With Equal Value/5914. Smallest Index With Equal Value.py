class Solution:
    def smallestEqual(self, nums):
        for i in range(len(nums)):
            if nums[i] % 10 == nums[i]:
                return i
        return -1


sol = Solution()
nums = [4, 3, 2, 1]
res = sol.smallestEqual(nums)
print(res)
