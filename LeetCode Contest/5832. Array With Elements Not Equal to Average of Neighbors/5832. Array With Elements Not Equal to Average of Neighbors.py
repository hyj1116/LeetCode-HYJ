from typing import List


class Solution:
    # def rearrangeArray(self, nums: List[int]) -> List[int]:
    #     for i in range(1, len(nums)-1):
    #         if nums[i]*2 == nums[i-1] + nums[i+1]:
    #             nums[i], nums[i+1] = nums[i+1], nums[i]
    #     nums.reverse()
    #     return nums
    def rearrangeArray(self, A):
        A.sort()
        n = len(A)
        A[::2], A[1::2] = A[n / 2:], A[:n / 2]
        return A


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5]
    nums = [42, 6, 10, 21, 26, 44, 31, 18, 25, 48, 35, 2, 29, 5, 20]
    sol = Solution()
    res = sol.rearrangeArray(nums)
    [20, 5, 29, 2, 35, 48, 25, 31, 18, 44, 26, 21, 10, 6, 42]

    print(res)
