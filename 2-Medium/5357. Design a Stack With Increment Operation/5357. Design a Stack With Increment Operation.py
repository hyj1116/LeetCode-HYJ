class CustomStack:
    vals = list()

    def __init__(self, maxSize):
        self.maxSize = maxSize

    def push(self, x):
        if len(self.vals) < self.maxSize:
            self.vals.append(x)
        print(self.vals)

    def pop(self):
        if len(self.vals) > 0:
            val = self.vals.pop()
            print(val)
            return val
        else:
            print(-1)
            return -1

    def increment(self, k, val):
        k = min(k, len(self.vals))
        for i in range(k):
            self.vals[i] += val


customStack = CustomStack(2)  # Stack is Empty []
customStack.push(35)                          # stack becomes [1]
customStack.pop()                          # stack becomes [1, 2]
# return 2 --> Return top of the stack 2, stack becomes [1]
customStack.increment(8, 100)
customStack.pop()                          # stack becomes [1, 2]
customStack.increment(9, 91)                        # stack becomes [1, 2, 3]
# stack still [1, 2, 3], Don't add another elements as size is 4
customStack.push(63)
customStack.pop()                # stack becomes [101, 102, 103]
customStack.push(84)                # stack becomes [201, 202, 103]
# return 103 --> Return top of the stack 103, stack becomes [201, 202]
customStack.increment(10, 93)
# return 202 --> Return top of the stack 102, stack becomes [201]
customStack.increment(6, 45)
# return 201 --> Return top of the stack 101, stack becomes []
customStack.increment(10, 4)
# return -1 --> Stack is empty return -1.

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
