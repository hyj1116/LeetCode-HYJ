# https://leetcode.com/problems/middle-of-the-linked-list/

print('__name__:', __name__)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListOperation:
    def middle_node(self, head):
        """Finds out one middle node

            Retrieves the middle node in the linked list, if there are 2 middle 
            nodes, return the second one.

            Args:
                head: The node points to the linked list.
                slow: The pointer traverse the linked list.
                fast: The pointer traverse as fast as twice as the 'slow' pointer.

            Returns:
                slow: 'slow' points to the middle node in the linked list finally.

            Analysis:
                Focus on better time complexity, we think of O(1), O(logN) and O(N).
                Since it asks us to find out the middle node in a linked 
                list, we consider O(N).
                Use two pointers 'fast' and 'slow' both point to head initially.
                The 'fast' traverse as fast as twice than 'slow'.
                        When 'fast' reaches the end of list, 'slow' is in the middle.
                E.g. 1-2-3-4-5 returns 3,  1-2-3-4-5-6 returns 4

            Pseudocode:
                fast, slow = head, head
                if not head: return None
                while fast.next
                    if not fast.next.next
                        return slow.next
                    fast = fast.next.next
                    slow = slow.next
                return slow
        """
        # Code
        # Corner case though its a non-empty list
        if not head:
            return None

        fast = slow = head  # The 'fast' and 'slow' pointers

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

        # Follow up:
        # Input: [1, 2, 3, 4, 5, 6]
        # Output: (Serialization: [4, 5, 6])
        # Follow up Aanswer:
        # while slow:
        #     print(slow.val, end=',')
        #     slow = slow.next


list_operation = ListOperation()


def test_middle_node(lists):

    for i, llist in enumerate(lists):
        curr = head = None
        for j in llist:
            if head is not None:
                curr.next = ListNode(j)
                curr = curr.next
            else:
                head = ListNode(j)
                curr = head
        print('TC{}:\t'.format(i+1), list_operation.middle_node(head))


if __name__ == "__main__":
    print('__name__:', "執行此檔案才會顯示")

    lists = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [6, 5, 4, 3, 2, 1],
        [1, 0, 5, 7, 2, 4, 3, 15, 8, 12],
    ]
    test_middle_node(lists)
