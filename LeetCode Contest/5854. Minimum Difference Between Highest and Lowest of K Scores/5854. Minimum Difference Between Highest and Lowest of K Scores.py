

class Solution:
    def minimumDifference(self, nums, k) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        nums.reverse()
        minimum = nums[0]
        for i in range(0, len(nums)-k+1):
            if nums[i]-nums[i+k-1] < minimum:
                minimum = nums[i]-nums[i+k-1]
        return minimum


if __name__ == '__main__':
    sol = Solution()
    nums = [64407, 3036]
    k = 2
    res = sol.minimumDifference(nums, k)
    print(res)
