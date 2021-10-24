class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res = 0
        if len(nums) < 3:
            return res
        second_beauty = True
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                for j in range(1, len(nums)-1):
                    if nums[j-1] < nums[j] < nums[j+1]:
                        res += 1
                return res
            return 2 * (len(nums)-2)

            #     second_beauty = True
            #     for j in range(i):
            #         if nums[j] > nums[j+1]:
            #             secode_beauty = False
            #     if secode_beauty:
            #         for j in range(i+1, len(nums)):
            #         if nums[j] > nums[j+1]:
            #             secode_beauty = False
            #         res+=2
            #     else:
            #         res+=1


sol = Solution()
nums = [3, 2, 1]
res = sol.sumOfBeauties(nums)
print(res)
