class Solution:
    def tictactoe(self, moves):
        #   A moves
        setA, setB = set(), set()
        for i in range(len(moves)):
            if i % 2:
                setB.add(moves[i][0] * 3 + moves[i][1]+1)
            else:
                setA.add(moves[i][0] * 3 + moves[i][1]+1)

        success = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
                   {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        for i in success:
            if len(i.difference(setA)) == 0:
                return "A"
        for i in success:
            if len(i.difference(setB)) == 0:
                return "B"
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"


if __name__ == "__main__":
    solution = Solution()
    my_list = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(solution.tictactoe(my_list))
