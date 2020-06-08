"""
Complexity Analysis

Time complexity : O(\log_{10}(n))O(log 
10
​	
 (n))

Because binary search cuts the search space roughly in half on each iteration, there can be at most \lceil \log_{10}(n) \rceil⌈log 
10
​	
 (n)⌉ iterations. Binary search is invoked twice, so the overall complexity is logarithmic.

Space complexity : O(1)O(1)

All work is done in place, so the overall memory usage is constant.
"""


class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

