from typing import List


class Solution:
    def pivotIndex(self, nums: 'List[int]') -> int:
        if not nums:
            return -1
        S = sum(nums)
        leftsum = 0
        for i, v in enumerate(nums):
            if leftsum == S - leftsum - nums[i]:
                return i
            leftsum += v
        return -1


sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(nums))
