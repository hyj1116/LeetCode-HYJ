class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        if min_index == 0:
            count = 0
        else:
            count = len(nums) - min_index
        print(min_index)
        # [3,4,5,1,2]
        for i in range(min_index-1):
            if nums[i+1] < nums[i]:
                return -1
        for i in range(min_index, len(nums)-1):
            if nums[i+1] < nums[i]:
                return -1
        if min_index != 0 and nums[-1] > nums [0]:
            return -1
        return count
        # for i in range(count):
        #     for k in range(len(nums)):
        #         nums[(k+1) % len(nums)] = nums[k]
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         return -1
        # return count
