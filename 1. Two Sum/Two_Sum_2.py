nums = [1, 12, 7, 5, 20, 1, 2]


class Solution:
    def twoSum(self, nums, target):
        """

        """
        # seen = {}
        for index, value in enumerate(nums):
            # print("index = %d" % index)
            # print("value = %d" % value)
            x = target-value
            if x in nums:
                return [nums.index(x), index]
            # else:
            #     seen[value] = index
            #     print(seen)


result = Solution()
print(result.twoSum(nums, 9))
