class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print(nums)
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right -left) // 2
            print(mid)
            if nums[mid] == target:
                if nums[mid+1] == target:
                    return [mid, mid+1]
                if nums[mid-1] == target:
                    return [mid-1, mid]
            elif nums[mid] < target:
                left = mid+1
            else:
                high = mid-1
        return [-1, -1]

        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         left_idx = i
        #         break
        # else:
        #     return [-1, -1]

        # # find the index of the rightmost appearance of `target` (by reverse
        # # iteration). it is guaranteed to appear.
        # for j in range(len(nums) - 1, -1, -1):
        #     if nums[j] == target:
        #         right_idx = j
        #         break

        # return [left_idx, right_idx]

nums = [5,7,7,8,8,10]
target = 8
sol = Solution()
res = sol.searchRange(nums)
print(res)
