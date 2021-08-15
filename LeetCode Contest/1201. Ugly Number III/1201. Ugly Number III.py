# https://leetcode.com/contest/weekly-contest-155/problems/ugly-number-iii/
class Solution:
    """
    Write a program to find the n-th ugly number.

    Input: n = 3, a = 2, b = 3, c = 5
    Output: 4
    Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
    """

    # Function to find the nth term divisible by a, b or c by using binary search
    def nthUglyNumber(self, a, b, c, n):

        # Set low to 1 and high to max (a, b, c) * n
        low = 1
        high = 10 ** 9
        mid = 0

        while low < high:
            mid = low + (high - low) // 2

            # If the current term is less than
            # n then we need to increase low
            # to mid + 1
            if divTermCount(a, b, c, mid) < n:
                low = mid + 1

            # If current term is greater than equal to
            # n then high = mid
            else:
                high = mid

        return low


# Function to return gcd of a and b
def gcd(a, b):

    if a == 0:
        return b

    return gcd(b % a, a)


# Function to return the lcm of a and b
def lcm(a, b):

    return (a * b) // gcd(a, b)


# Function to return the count of numbers from 1 to num which are divisible by a, b or c
def divTermCount(a, b, c, num):

    # Calculate number of terms divisible by a and
    # by b and by c then, remove the terms which is are
    # divisible by both a and b, both b and c, both
    # c and a and then add which are divisible by a and
    # b and c
    return (
        (num // a)
        + (num // b)
        + (num // c)
        - (num // lcm(a, b))
        - (num // lcm(b, c))
        - (num // lcm(a, c))
        + (num // lcm(a, lcm(b, c)))
    )


# Driver code
a = 3
b = 2
c = 3
n = 5
res = Solution()
print(res.nthUglyNumber(a, b, c, n))

