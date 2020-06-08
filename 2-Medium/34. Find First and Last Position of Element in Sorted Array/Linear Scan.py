"""
Complexity Analysis

Time complexity : O(n)O(n)

This brute-force approach examines each of the n elements of nums exactly twice, so the overall runtime is linear.

Space complexity : O(1)O(1)

The linear scan method allocates a fixed-size array and a few integers, so it has a constant-size memory footprint.
"""


class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


sol = Solution()
nums = [1, 2, 3, 4, 5]
print(sol.searchRange(nums, 2))

