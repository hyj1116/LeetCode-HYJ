class Solution:
    def maxScore(self, cardPoints, k):
        # left_sum = cardPoints[0]
        # right_sum = cardPoints[-1]
        # new_cards = sorted(cardPoints[1:], reverse=True)
        # print(new_cards)

        # for i in range(k-1):
        #     left_sum += new_cards[i]
        # new_cards = sorted(cardPoints[:-1], reverse=True)
        # print(new_cards)

        # for i in range(k-1):
        #     right_sum += new_cards[i]

        # return max(left_sum, right_sum)


if __name__ == "__main__":
    solution = Solution()
    my_list = [1, 79, 80, 1, 1, 1, 200, 1]
    print(solution.maxScore(my_list, 3))
