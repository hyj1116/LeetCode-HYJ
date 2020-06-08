# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head):
        num = []
        res = 0
        while head:
            num.append(head.val)
            head = head.next
        length = len(num)
        for i in range(length):
            print(num[i])
            print(num[i]*2)
            print(length)
            print(length-1-i)
            print((num[i]*2)**(length-1-i))
            res += num[i]*(num[i]*2)**(length-1-i)
        return res


if __name__ == "__main__":
    solution = Solution()
    # head1 = ListNode(1)
    # head2 = ListNode(0)
    # head3 = ListNode(1)
    # head1.next = head2
    # head2.next = head3
    head1 = ListNode(0)
    print(solution.getDecimalValue(head1))
