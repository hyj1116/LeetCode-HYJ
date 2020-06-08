nums = [100, 2, 12, 7, 5, 20, 1, 3]


class Solution:
    def twoSum(self, nums, target):
        """
            asds
            """
        """
        """
        seen = {}
        for index, value in enumerate(nums):
            print("index = %d" % index)
            print("value = %d" % value)
            if target - value in seen:
                return [seen[target - value], index]
            seen[value] = index
            print(seen)


result = Solution()
print(result.twoSum(nums, 9))
