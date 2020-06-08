# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution:
    def trap(self, height):
        sum = 0
        for i in range(1, len(height) - 1):
            max_left = max(height[: i + 1])
            max_right = max(height[i:])
            sum += min(max_left, max_right) - height[i]
        return sum


nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
print(sol.trap(nums))
