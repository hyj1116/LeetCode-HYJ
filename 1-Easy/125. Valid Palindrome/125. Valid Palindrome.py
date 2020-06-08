
import random


class Solution:
    def is_palindrome(self, s):
        palindromeString = [i.lower() for i in s if i.isalnum()]
        return palindromeString == palindromeString[::-1]


sol = Solution()
my_list = "race a car"
print(sol.is_palindrome(my_list))
