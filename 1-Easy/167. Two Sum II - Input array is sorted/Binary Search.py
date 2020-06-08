class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1


nums = [1, 2, 3, 4, 4, 9, 56, 90]
sol = Solution()
sol.twoSum(nums, 8)
