class Solution:
    def freqAlphabets(self, s):
        res = ""
        left = right = 0
        ch = ""
        stack = []
    #   Stack解法
        for i in range(len(s)):
            if s[i] != '#' and len(stack) != 2:
                stack.append(s[i])
            elif s[i] == '#':
                left = int(stack.pop())
                right = int(stack.pop()) * 10
                ch = chr(ord('a') + right + left - 1)
                res += ch
            elif len(stack) == 2:
                right = chr(ord('a') + int(stack.pop()) - 1)
                res += left
                res += right
                stack.append(s[i])

        while len(stack) != 0:
            right = chr(ord('a') + int(stack.pop()) - 1)
            left = chr(ord('a') + int(stack.pop()) - 1)
            res += left
            res += right
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
    print(solution.freqAlphabets(s))
