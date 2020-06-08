class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev


import random
if __name__ == "__main__":
    solution = Solution()
    my_list = random.choices(range(10), k=10)
    print(solution(my_list))
    