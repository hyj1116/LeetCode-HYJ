# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:  # 這裡之所以判斷fast.next是因為之後會用到fast = fast.next.next，若此時只判斷fast是否為None而不判斷fast.next，若fast.next為None，則後續的fast.next.next會傳回 AttributeError 'NoneType' has no attribute of 'next'的錯誤
            fast = fast.next.next
            slow = slow.next
        stack = []
        while slow:
            stack.append(slow.val)
            slow = slow.next
        while head:
            if stack.pop != head.val:
                return False
            head = head.next
        return True
