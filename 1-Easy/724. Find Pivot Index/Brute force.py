class Solution:
    def pivotIndex(self, nums):
        """
        Brute force
        """
        if not nums:
            return -1
        S = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            leftsum = 0
            for j in range(0, i):
                leftsum += nums[j]
            if leftsum == S - leftsum - nums[i]:
                return i
        return -1


sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(nums))
