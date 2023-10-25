class ListNode:
    def __init__(self, value):
        self.value = value    # 儲存節點的值
        self.next = None      # 指向下一個節點的引用

    def fn(head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
