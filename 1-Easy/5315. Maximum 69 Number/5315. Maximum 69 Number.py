

class Solution:
    def maximum69Number(self, num):
        res = 0
        s = str(num)
        li = list(s)
        for i in range(len(li)):
            if li[i] == '6':
                li[i] = '9'
                break
        for i in range(len(li)):
            res += int(li[i])*(10**(len(li)-1-i))
        return res
    # solution 2
    str.replace

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximum69Number(9696))
