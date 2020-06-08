from collections import defaultdict


class Leaderboard:

    def __init__(self):
        # self.val = defaultdict(int)
        self.val = {}

    def addScore(self, playerId, score):
        if self.val.get(playerId) != None:
            self.val[playerId] += score
        else:
            self.val[playerId] = score
            # i = self.val.index(playerId)
            # self.val[i] = [playerId, score]

    def top(self, K):
        temp = sorted(self.val.values(), reverse=True)
        sum = 0
        for i in range(K):
            sum += temp[i]
        print(sum)

    def reset(self, playerId):
        self.val[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
if __name__ == "__main__":
    # ["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
    # [[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
    leaderboard = Leaderboard()
    leaderboard.addScore(1, 13)
    leaderboard.addScore(2, 93)
    leaderboard.addScore(3, 84)
    leaderboard.addScore(4, 6)
    leaderboard.addScore(5, 89)
    leaderboard.addScore(6, 31)
    leaderboard.addScore(7, 7)
    leaderboard.addScore(8, 1)
    leaderboard.addScore(9, 98)
    leaderboard.addScore(10, 42)
    leaderboard.top(5)
    leaderboard.reset(1)
    leaderboard.reset(2)
    leaderboard.addScore(3, 76)
    leaderboard.addScore(4, 68)
    leaderboard.top(1)
    leaderboard.reset(3)
    leaderboard.reset(4)
    leaderboard.addScore(2, 70)
    leaderboard.reset(2)
    for i in leaderboard.val:
        print(i, leaderboard.val[i])
["Leaderboard", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore", "addScore",
    "addScore", "addScore", "top", "reset", "reset", "addScore", "addScore", "top", "reset", "reset", "addScore", "reset"]
[[], [1, 13], [2, 93], [3, 84], [4, 6], [5, 89], [6, 31], [7, 7], [8, 1], [
    9, 98], [10, 42], [5], [1], [2], [3, 76], [4, 68], [1], [3], [4], [2, 70], [2]]
