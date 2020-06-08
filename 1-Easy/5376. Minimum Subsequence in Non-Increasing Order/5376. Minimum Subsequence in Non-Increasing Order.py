class Solution:
    def minSubsequence(self, nums):
        total = 0
        for i in nums:
            total += i
        total //= 2
        li = []
        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]
                if temp_sum > total:
                    li.append(nums[i:j+1])
                    break
        res = sorted(li, key=lambda i: len(i))
        length = len(res[0])
        temp_res = []
        for i in res:
            if len(i) == length:
                temp_res.append(i)
        res = sorted(temp_res, key=lambda i: sum(i), reverse=True)
        return sorted(res[0], key=lambda i: i, reverse=True)


if __name__ == "__main__":
    solution = Solution()
    nums = [7, 4, 2, 8, 1, 7, 7, 10]
    print(solution.minSubsequence((nums)))
