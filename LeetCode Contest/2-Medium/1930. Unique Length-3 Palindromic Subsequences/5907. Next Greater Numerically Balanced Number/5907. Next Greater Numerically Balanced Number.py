class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        notFound = True
        num = n+1
        while notFound:
            dic = {}
            for i in str(num):
                if int(i) not in dic:
                    dic[int(i)] = 1
                else:
                    dic[int(i)] += 1
            for i in dic:
                if int(i) != dic[int(i)]:
                    notFound = True
                    break
                notFound = False
            if notFound == False:
                return num
            num += 1


sol = Solution()
num = 1
res = sol.nextBeautifulNumber(num)

print(res)
