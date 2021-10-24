class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        dic = {}
        res = 0
        for i in range(len(properties)-1):
            for j in range(i+1, len(properties)):
                if properties[i][0] > properties[j][0]:
                    if properties[i][1] > properties[j][1]:
                        dic[(properties[j][0], properties[j][1], j)] = True
                elif properties[i][0] < properties[j][0]:
                    if properties[i][1] < properties[j][1]:
                        dic[(properties[i][0], properties[i][1], i)] = True
                print(dic)
        return len(dic)


if __name__ == '__main__':
    sol = Solution()
    properties = [[7, 7], [1, 2], [9, 7], [7, 3], [
        3, 10], [9, 8], [8, 10], [4, 3], [1, 5], [1, 5]]
    res = sol.numberOfWeakCharacters(properties)
    print(res)
