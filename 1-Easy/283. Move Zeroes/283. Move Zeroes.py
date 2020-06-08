class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         res.append(nums[i])
        #         nums.pop(i)
        # res.extend(nums)

        ### In-place Solution ###
        # zero_index = -1
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zero_index = i
        #         break
        # if zero_index != -1:
        #     for i in range(zero_index+1, len(nums)):
        #         if nums[i] != 0:
        #             nums[zero_index] = nums[i]
        #             nums[i] = 0
        #             zero_index += 1

        ### In-place Solution ###
        lastNonZeroFoundAt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.moveZeroes(([4, 2, 4, 0, 0, 3, 0, 5, 1, 0])))
