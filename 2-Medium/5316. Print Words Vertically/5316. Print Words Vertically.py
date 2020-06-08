class Solution:
    def printVertically(self, s):
        # """
        # Output: ["HAY","ORO","WEU"]
        # Explanation: Each word is printed vertically.
        # "HAY"
        # "ORO"
        # "WEU"
        # """
        res = []
        s_list = s.split(' ')
        max_len = 0
        for _ in s_list:
            if len(_) > max_len:
                max_len = len(_)
        for i in range(len(s_list)):
            if len(s_list[i]) < max_len:
                s_list[i] += (max_len - len(s_list[i])) * ' '
        print(s_list)
        print(max_len)
        for i in range(max_len):
            temp = ''
            for j in s_list:
                temp += j[i]
            res.append(temp)
        for i in range(len(res)):
            res[i] = res[i].rstrip(" ")
        return res


if __name__ == "__main__":
    solution = Solution()
    s = "HOW ARE YOU"
    s = "TO BE OR NOT TO BE"
    print(solution.printVertically(s))
