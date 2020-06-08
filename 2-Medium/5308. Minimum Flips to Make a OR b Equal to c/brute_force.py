class Solution:
    def minFlips(self, a, b, c):
        res = 0
        str_a = bin(a)[2::]
        str_b = bin(b)[2::]
        str_c = bin(c)[2::]
        len_max = max(len(str_a), len(str_b), len(str_c))
        str_a = '0' * (len_max-len(str_a)) + str_a
        str_b = '0' * (len_max-len(str_b)) + str_b
        str_c = '0' * (len_max-len(str_c)) + str_c
        for i in range(len_max, 0, -1):
            int_a = int(str_a[i-1])
            int_b = int(str_b[i-1])
            int_c = int(str_c[i-1])
            if (int_a or int_b) != int_c:
                if int_c == 1:
                    res += 1
                else:
                    res += abs(int_a+int_b-int_c)
        return res


if __name__ == "__main__":
    solution = Solution()
    a = 2
    b = 6
    c = 5
    print(solution.minFlips(a, b, c))
