class Solution:
    def reorderLogFiles(self, logs):
        a = []  # letter-logs
        b = []  # digit-logs
        # logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        for i in logs:
            if i.split(" ")[1].isdigit():
                b.append(i)
            else:
                a.append(i)
        print(a)
        print(b)
        a = sorted(a, key=lambda item: (item.split(" ")[1:], item.split()[0]))
        return a+b


if __name__ == "__main__":
    sol = Solution()
    sol.reorderLogFiles(["dig1 8 1 5 1", "let1 art can",
                         "dig2 3 6", "let2 own kit dig", "let3 art zero"])
