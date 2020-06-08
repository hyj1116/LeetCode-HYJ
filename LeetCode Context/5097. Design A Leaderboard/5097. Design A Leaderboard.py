from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.val = defaultdict(list)
        # self.val = []

    def addScore(self, playerId, score):
        self.val[playerId].append(score)
        # i = self.val.index(playerId)
        # self.val[i] = [playerId, score]

    def top(self, K):
        # self.val.sort(key=val[])
        # [(k,di[k]) for k in sorted(di.keys())]
        # sorted(dict1.items(), key=lambda d: d[1])
        temp = sorted(self.val.items(), key=lambda k_v: k_v[1][1])

        sum = 0
        for i in range(K):
            sum += temp[i][1][1]
        return sum

    def reset(self, playerId):
        self.val.pop([playerId])


# Your Leaderboard object will be instantiated and called as such:
if __name__ == "__main__":
    # ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
    # [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]

    obj = Leaderboard()
    print(obj)
    obj.addScore(3, 39)
    # for k in obj.val:
    #     print(k, k[1])
    param_2 = obj.top(1)
    obj.reset(3)
