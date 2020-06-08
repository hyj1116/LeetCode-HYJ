
class Solution:
    def rankTeams(self, votes):
        res = {}

        dic = {}
        for i in votes:
            for j in range(len(i)):
                if res[dic[i][j]] == 0:
                    res[dic[i][j]] += 1
                else:
                    res[dic[i][j]] += j
        res2 = sorted(res.keys())
        return res2


if __name__ == "__main__":
    solution = Solution()
    votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    print(solution.rankTeams(votes))
