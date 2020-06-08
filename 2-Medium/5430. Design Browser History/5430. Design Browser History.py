class BrowserHistory:
    # stack = []
    # current = 0

    def __init__(self, homepage: str):
        self.stack = [homepage]
        # self.stack.append(homepage)
        self.current = 1

    def visit(self, url: str) -> None:
        while len(self.stack) > self.current:
            self.stack.pop()
        self.stack.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        if self.current > steps:
            self.current -= steps
        else:
            self.current = 1
        return self.stack[self.current-1]

    def forward(self, steps: int) -> str:
        if self.current + steps < len(self.stack):
            self.current += steps
        else:
            self.current = len(self.stack)
        return self.stack[self.current-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

if __name__ == "__main__":
    browserHistory = BrowserHistory("leetcode.com")
    browserHistory.visit("google.com")
    # // You are in "leetcode.com". Visit "google.com"
    browserHistory.visit("facebook.com")
    # // You are in "google.com". Visit "facebook.com"
    browserHistory.visit("youtube.com")
    # // You are in "facebook.com". Visit "youtube.com"
    browserHistory.back(1)
    # // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    browserHistory.back(1)
    # // You are in "facebook.com", move back to "google.com" return "google.com"
    browserHistory.forward(1)
    # // You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browserHistory.visit("linkedin.com")
    # // You are in "facebook.com". Visit "linkedin.com"
    browserHistory.forward(2)
    # // You are in "linkedin.com", you cannot move forward any steps.
    browserHistory.back(2)
    # // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    browserHistory.back(7)
    # // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
