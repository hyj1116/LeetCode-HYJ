class Solution:
    def helper(self, num, count):
        if num == 0:
            return count
        elif num % 2:
            num -= 1
        else:
            num /= 2
        return self.helper(num, count+1)

    def numberOfSteps(self, num: int) -> int:
        return self.helper(num, 0)
