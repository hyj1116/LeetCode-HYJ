# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListOperation:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        next_node = head.next  # head -> next_node
        next_node.next = head  # head <- next_node
        head.next = None         # [x] <- head <- next_node
        return new_head


def test_middle_node(lists):
    list_operation = ListOperation()
    for i, llist in enumerate(lists):
        curr = head = None
        for j in llist:
            if head is not None:
                curr.next = ListNode(j)
                curr = curr.next
            else:
                head = ListNode(j)
                curr = head
        print('TC{}:\t'.format(i+1), list_operation.reverseList(head))


if __name__ == "__main__":
    print('__name__:', "執行此檔案才會顯示")

    lists = [
        [1, 2, 3],
    ]
    test_middle_node(lists)
