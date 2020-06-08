# https://leetcode.com/problems/trapping-rain-water/solution/
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = max_l = max_r = 0
        l = 0
        r = len(height) - 1
        while l < r:
            # if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            if height[r] > max_r:
                max_r = height[r]
            if max_l < max_r:
                areas += max_l - height[l]
                l += 1
            else:
                areas += max_r - height[r]
                r -= 1
        return areas


nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
sol = Solution()
print(sol.trap(nums))
